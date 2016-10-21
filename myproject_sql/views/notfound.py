# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pyramid.view import notfound_view_config


@notfound_view_config(renderer='../templates/404.jinja2')
def notfound_view(request):
    """Will route people to the 404 not-found page."""
    # import pdb; pdb.set_trace()
    request.response.status = 404
    return {}
