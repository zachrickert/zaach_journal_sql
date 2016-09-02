# import os
# import pytest

# from pyramid import testing

# def test_public_view_accessible(app):
#     response = app.get('/public')
#     assert response.status_code == 200


# def test_public_view_inaccessible(app):
#     response = app.get('/private' status ='4*')
#     assert response.status_code == 403

# comment this out first. Will fail for a while.-------------------

# def test_private_view_accessible(app):
#     response = app.get('/private')
#     assert response.status_code == 200

# -----------------------------------------------------------------

# def test_auth_user_name_exists(auth_env):
#     assert os.environ.get('AUTH_USERNAME') is not None


# def test_auth_user_name_is_not_empty(auth_env):
#     assert os.environ.get('AUTH_USERNAME') != ''

# def test_auth_password_exisits(auth_env):
#     assert os.environ.get('AUTH_PASSWORD') is not None

# def test_auth_user_password_is_not_empty(auth_env):
#     assert os.environ.get('AUTH_PASSWORD') != ''

# def test_user_name_is_good(auth_env):
#     from test_transactions.security import check_creditentials
#     assert check_creditentials('billy')




