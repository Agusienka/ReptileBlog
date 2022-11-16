from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kurwa@localhost:5432/ReptileBlog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False     
app.config['SECRET_KEY'] = '1e3c6de625d9304cd306a49eaba9b47b'   
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from . import models

models.db.init_app(app)
migrate = Migrate(app, models.db)

from reptileBlog import routes

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kurwa@localhost/ReptileBlog'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False





# from reptileBlog import routes
