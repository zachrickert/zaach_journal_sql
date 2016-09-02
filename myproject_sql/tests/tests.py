import pytest
import transaction

from pyramid import testing
from datetime import datetime

from ..models import (
    Entry,
    get_engine,
    get_session_factory,
    get_tm_session,
)
from ..models.meta import Base

DB_SETTINGS = {'sqlalchemy.url': 'sqlite:////tmp/testme.sqlite'}

@pytest.fixture(scope="session")
def sqlengine(request):
    config = testing.setUp(settings=DB_SETTINGS)
    config.include("..models")
    settings = config.get_settings()
    engine = get_engine(settings)
    Base.metadata.create_all(engine)

    def teardown():
        testing.tearDown()
        transaction.abort()
        Base.metadata.drop_all(engine)

    request.addfinalizer(teardown)
    return engine


@pytest.fixture(scope="function")
def new_session(sqlengine, request):
    session_factory = get_session_factory(sqlengine)
    session = get_tm_session(session_factory, transaction.manager)

    def teardown():
        transaction.abort()

    request.addfinalizer(teardown)
    return session


@pytest.fixture(scope="function")
def populated_db(request, sqlengine):
    session_factory = get_session_factory(sqlengine)
    session = get_tm_session(session_factory, transaction.manager)

    with transaction.manager:
        session.add(Entry(title="Day 15", body="This is a test entry, James is being awesome.", creation_date=datetime.utcnow()))

    def teardown():
        with transaction.manager:
            session.query(Entry).delete()

    request.addfinalizer(teardown)


@pytest.fixture()
def dummy_request(new_session):
    """Call a dummy request."""
    return testing.DummyRequest(dbsession=new_session)


def test_model_gets_added(new_session):
    assert len(new_session.query(Entry).all()) == 0
    model = Entry(title="Bob", body="Test")
    new_session.add(model)
    new_session.flush()
    assert len(new_session.query(Entry).all()) == 1


def test_home_view(dummy_request, new_session):
    """Test entries on the home view."""
    from ..views.views import my_view
    new_session.add(Entry(title='the title', body='the body', creation_date=datetime.utcnow()))
    new_session.flush()
    info = my_view(dummy_request)
    # import pdb; pdb.set_trace()
    assert info['entries'][0].title == 'the title'


def test_create_view(dummy_request, new_session):
    """Test entries on the home view."""
    from ..views.views import create
    info = create(dummy_request)
    assert info == {}


# def test_create_view(dummy_request, new_session):
#     """Test entries on the home view."""
#     from ..views.views import create
#     info = create(dummy_request)


# ----------Functional--------------------

@pytest.fixture()
def testapp(sqlengine):
    from myproject_sql import main
    app = main({}, **DB_SETTINGS)
    from webtest import TestApp
    return TestApp(app)


def test_layout_main(testapp, populated_db):
    response = testapp.get('/', status=200)
    assert b'Day 15' in response.body


def test_layout_single_entry(testapp, populated_db):
    response = testapp.get('/journal/1', status=200)
    assert b'This is a test entry' in response.body


def test_layout_edit_entry(testapp, populated_db):
    response = testapp.get('/journal/1/edit-entry', status=200)
    assert b'This is a test entry' in response.body


def test_layout_create_entry(testapp, populated_db):
    response = testapp.get('/journal/new-entry', status=200)
    assert b'Title:' in response.body


