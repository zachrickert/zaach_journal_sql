from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from ..models import MyModel


# @view_config(route_name='home', renderer='../templates/mytemplate.jinja2')
# def my_view(request):
#     try:
#         query = request.dbsession.query(MyModel)
#         one = query.filter(MyModel.name == 'one').first()
#     except DBAPIError:
#         return Response(db_err_msg, content_type='text/plain', status=500)
#     return {'one': one, 'project': 'MyProject_sql'}


# # in views/default.py

# @view_config(route_name="edit", renderer="../templates/edit-model.jinja2")
# def edit_view(request):
#     if request.method == "POST":
#         new_name = request.POST["name"]
#         new_val = request.POST["value"]
#         new_model = MyModel(name=new_name, value=new_val)

#         request.dbsession.add(new_model)

#         return {"data": {"name": "We made a new model!"}}

#     return {"data": {"name": "A New Form"}}


db_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_MyProject_sql_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""
