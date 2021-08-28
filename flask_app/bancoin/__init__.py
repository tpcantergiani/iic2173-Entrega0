from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
# from flask import render_template, url_for, flash, redirect, request
from flask_cors import CORS
import os
from flask_mail import Mail
from dotenv import load_dotenv, find_dotenv

app = Flask(__name__)
load_dotenv(find_dotenv())

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

cors = CORS(app)

if os.environ.get('FLASK_ENV') == 'production':
    print("*"*15+"production is true"+"*"*15)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
else:
    print(" * "*15+"production is false"+" * "*15)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.environ.get('DB_USERNAME')}:{os.environ.get('DB_PASSWORD')}@postgres:5432/{os.environ.get('DB_NAME')}"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['CORS_HEADERS'] = 'Content-Type'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# app.config['MAIL_SERVER']= os.environ.get('MAIL_SERVER')
# app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT'))
# app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
# app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
# app.config['MAIL_USE_TLS'] = (os.environ.get('MAIL_USE_TLS') == 'True')
# app.config['MAIL_USE_SSL'] = (os.environ.get('MAIL_USE_SSL') == 'True')
# app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_SENDER')

# mail = Mail(app)


import bancoin.routes

