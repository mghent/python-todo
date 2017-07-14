from flask import render_template
from app.extensions import celery
from app.models import db
from celery.signals import task_postrun


@celery.task
def do_task():
    return 0


@task_postrun.connect
def close_session(*args, **kwargs):
    # Flask SQLAlchemy will automatically create new sessions for you from
    # a scoped session factory, given that we are maintaining the same app
    # context, this ensures tasks have a fresh session (e.g. session errors
    # won't propagate across tasks)
    db.session.remove()