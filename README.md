# mini-todo

A mini Flask project

## What I Implemented

- CRUD action
- Form validation with [WTForms](https://wtforms.readthedocs.io/en/stable/)
- Database migration with [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/)
- Database ORM with [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

## How to Launch (Windows)

1. `git clone` this repository
1. `cd` into the clonned repository's directory
1. Create python virtual environment: `python -m venv venv`. [Read more](https://docs.python.org/3/library/venv.html#creating-virtual-environments)
1. Activate the python venv: `venv\scripts\activate`. [Read more](https://flask.palletsprojects.com/en/1.1.x/installation/#activate-the-environment)
1. Install dependencies: `pip install .`
1. [`set FLASK_APP=mini_todo`](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application)
1. Run app: `flask run`

## Note

`Commands` may differ depending on your OS.
