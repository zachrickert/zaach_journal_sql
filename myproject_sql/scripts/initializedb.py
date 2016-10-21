import os
import sys
import transaction
from datetime import datetime

from pyramid.paster import (
    get_appsettings,
    setup_logging,
)

from pyramid.scripts.common import parse_vars

from ..models.meta import Base
from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
)
from ..models.mymodel import Entry

from ..views import TIME_FORMAT


ENTRIES = [
    {"title": "Testing Coverage", "creation_date": "2016-08-22 10:00:00", "id": 12, "body": "I worked with Will a little bit about testing and I feel like I have a better undestanding of testing.  He clued me in on:\n\npy.test --cov=src --cov-report=term-missing\n\nThis will give you the coverage tests, but also show you which lines your code didn't hit."},
    {"title": "Http Server Classes", "creation_date": "2016-08-22 10:00:00", "id": 11, "body": "Today I put the response / request functions of the http server into calsses.\nI was really happy with the results and I think it was a useful exercise to do.\nMy next goal is to use the properties method in classes. \nAlso I learned today that is the server has a print line in it's implimentation it causes the whole system to hang.  It took my a long time to figure that out."},
    {"title": "File Path Name", "creation_date": "2016-08-22 10:00:00", "id": 10, "body": "os.path.isdir(target) - determines if the target is a directory.\nos.path.abspath(target) - gets the absolute path to the file.\nos.path.join() - joins two paths together.\nWill return an absolute path if one is an absolute path"},
]


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    
    settings['sqlalchemy.url'] = os.environ['DATABASE_URL']
    engine = get_engine(settings)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    session_factory = get_session_factory(engine)

    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)
        for entry in ENTRIES:
            this_entry = Entry(title=entry['title'], body=entry['body'], creation_date=datetime.strptime(entry['creation_date'], TIME_FORMAT))
            dbsession.add(this_entry)
