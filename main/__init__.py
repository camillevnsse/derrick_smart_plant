from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test_database.db"
db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins='*')

from main import routes