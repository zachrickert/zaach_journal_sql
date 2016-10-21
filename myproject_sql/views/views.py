# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pyramid.view import view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPNotFound, HTTPFound
from sqlalchemy.exc import DBAPIError
from datetime import datetime

from ..models import Entry
import os

HERE = os.path.dirname(__file__)
TIME_FORMAT = '%Y-%m-%d %I:%M:%S'


@view_config(route_name='home', renderer='../templates/index.jinja2')
def my_view(request):
    query = request.dbsession.query(Entry)
    list_of_entries = query.order_by(Entry.creation_date.desc()).all()
    return {'title': 'Home', 'entries': list_of_entries}


@view_config(route_name='create', renderer='../templates/edit_entry.jinja2')
def create(request):
    if request.method == "POST":
        new_title = request.POST["title"]
        new_body = request.POST["body"]
        new_date = datetime.now()
        new_model = Entry(title=new_title, body=new_body, creation_date=new_date)

        request.dbsession.add(new_model)

        url = request.route_url('home')
        return HTTPFound(location=url)
        # return {'id': id, 'title': new_title, 'creation_date': new_date, 'body': new_body}
    return {}

@view_config(route_name='detail', renderer='../templates/single_entry.jinja2')
@view_config(route_name='edit', renderer='../templates/edit_entry.jinja2')
def edit_view(request):
    id = request.matchdict.get('id', None)
    query = request.dbsession.query(Entry)
    entry = query.filter(Entry.id == id).first()
    if entry is None:
        raise HTTPNotFound

    if request.method == "POST":
        # import pdb; pdb.set_trace()
        new_title = request.POST["title"]
        new_body = request.POST["body"]
        
        entry.title = new_title
        entry.body = new_body

        # url = request.route_url('detail', id=entry.id)
        url = request.route_url('home')
        return HTTPFound(location=url)

    return {'id': id, 'title': entry.title, 'creation_date': entry.creation_date, 'body': entry.body}

