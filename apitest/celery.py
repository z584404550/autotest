from __future__ import absolute_import
from celery import Celery
from django.conf import settings
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'autotest.settings')
django.setup()
app = Celery('autotest')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
