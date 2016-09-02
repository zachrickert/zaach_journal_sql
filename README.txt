MyProject_sql README
==================

Author
---------------
Zach Rickert
zachrickert@gmail.com


Getting Started
---------------

- cd <directory containing this file>

- $VENV/bin/pip install -e .

- $VENV/bin/initialize_MyProject_sql_db development.ini

- $VENV/bin/pserve development.ini


-----------------
pytest coverage
------------------

---------- coverage: platform darwin, python 3.5.2-final-0 -----------
Name                                          Stmts   Miss  Cover
-----------------------------------------------------------------
myproject_sql/__init__.py                         9      0   100%
myproject_sql/models/__init__.py                 22      0   100%
myproject_sql/models/meta.py                      5      0   100%
myproject_sql/models/mymodel.py                  13      0   100%
myproject_sql/routes.py                           6      0   100%
myproject_sql/scripts/__init__.py                 0      0   100%
myproject_sql/scripts/initializedb.py            31     18    42%
myproject_sql/views/__init__.py                   1      0   100%
myproject_sql/views/default.py                    5      0   100%
myproject_sql/views/notfound.py                   4      2    50%
myproject_sql/views/views.py                     44     18    59%
-----------------------------------------------------------------
TOTAL                                           140     38    73%

7 passed in 1.16 seconds
___________________________________________________________ summary ___________________________________________________________
  py27: commands succeeded
  py35: commands succeeded
