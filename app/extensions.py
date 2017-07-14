from flask_restless import APIManager
api = APIManager()

from celery import Celery
celery = Celery()

from flask_babel import Babel
babel = Babel()