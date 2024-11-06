from datetime import timedelta

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.secret_key = 'abc123'

app.config['SQLALCHEMY_ECHO'] = True

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:rootroot@localhost:3306/signet'

app.config['SQLALCHEMY_MAX_OVERFLOW'] = 0

db = SQLAlchemy(app)
app.app_context().push()
from base.com import controller
