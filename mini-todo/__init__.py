from uuid import uuid4

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# --------------
# Initialization
# --------------

app = Flask(__name__)
app.secret_key = uuid4().bytes
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

migrate = Migrate(app, db)

if app and db:
    import views  # Go to 'views.py'
