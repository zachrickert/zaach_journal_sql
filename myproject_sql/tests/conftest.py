# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pyramid import testing

import pytest

@pytest.fixture()
def dummy_request(new_session):
    """Return a dummy request."""
    return testing.DummyRequest(dbsession=new_session)
