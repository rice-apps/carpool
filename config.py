import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

APP_URL = 'http://127.0.0.1:5000/'

CAS_SERVER = 'https://netid.rice.edu'
CAS_AFTER_LOGIN = 'index'

WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'