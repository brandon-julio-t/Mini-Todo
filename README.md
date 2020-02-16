[![](https://img.shields.io/badge/status-Finished-brightgreen)]()
[![](https://img.shields.io/github/last-commit/brandon-julio-t/Mini-Todo)]()

# Mini Todo

## What I Implemented

- Implemented CRUD action
- Uses [WTForms](https://wtforms.readthedocs.io/en/stable/) as form validation
- Uses [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) as database migration
- Uses [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) as database ORM
- Uses [Bootstrap](https://getbootstrap.com/) to design front-end
- Uses [SQLite](https://sqlite.org/index.html) as database engine

## How to Launch (Windows)

1. `git clone` this repository
1. `cd` into the clonned repository's directory
2. Create python virtual environment: `python -m venv venv`.
3. Activate the python venv: `venv\scripts\activate`. [Linux](https://flask.palletsprojects.com/en/1.1.x/installation/#activate-the-environment)
4. Install dependencies: `pip install -r requirements.txt`
5. Set environment variable: [CMD: [`set FLASK_APP=mini_todo`] | PowerShell: `$env:FLASK_APP="mini_todo"`](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application)
6. Run app: `flask run`

## Note

`Commands` may differ depending on your OS.
