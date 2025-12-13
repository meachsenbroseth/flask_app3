from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from authlib.integrations.flask_client import OAuth
from flask_login import LoginManager

db = SQLAlchemy()
oauth = OAuth()
csrf = CSRFProtect()
login_manager = LoginManager()