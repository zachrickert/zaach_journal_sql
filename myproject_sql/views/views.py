from pyramid.view import view_config
import os

HERE = os.path.dirname(__file__)

ENTRIES = [
    {"title": "Testing Coverage", "creation_date": "Aug 22, 2016", "id": 12, "body": "I worked with Will a little bit about testing and I feel like I have a better undestanding of testing.  He clued me in on:\n\npy.test --cov=src --cov-report=term-missing\n\nThis will give you the coverage tests, but also show you which lines your code didn't hit."},
    {"title": "Http Server Classes", "creation_date": "Aug 21, 2016", "id": 11, "body": "Today I put the response / request functions of the http server into calsses.\nI was really happy with the results and I think it was a useful exercise to do.\nMy next goal is to use the properties method in classes. \nAlso I learned today that is the server has a print line in it's implimentation it causes the whole system to hang.  It took my a long time to figure that out."},
    {"title": "File Path Name", "creation_date": "Aug 20, 2016", "id": 10, "body": "os.path.isdir(target) - determines if the target is a directory.\nos.path.abspath(target) - gets the absolute path to the file.\nos.path.join() - joins two paths together.\nWill return an absolute path if one is an absolute path"},
]

@view_config(route_name='home', renderer='../templates/index.jinja2')
def list_view(request):
    return {'title': 'Home',
            "entries": ENTRIES
            }


@view_config(route_name='create', renderer='../templates/new_entry.jinja2')
def create(request):
    return {'title': 'New Entry'}


@view_config(route_name='detail', renderer='../templates/single_entry.jinja2')
def detail_view(request):
    id = request.matchdict.get('id', None)
    for entry in ENTRIES:
        if entry['id'] == int(id):
            return entry


@view_config(route_name='edit', renderer='../templates/edit_entry.jinja2')
def edit_view(request):
    id = request.matchdict.get('id', None)
    for entry in ENTRIES:
        if entry['id'] == int(id):
            return entry


# def includeme(config):
#     config.add_view(list_view, route_name='home')
#     config.add_view(create, route_name='create')
#     config.add_view(detail_view, route_name='detail')
#     config.add_view(edit_view, route_name='edit')
