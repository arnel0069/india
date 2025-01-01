"""
WSGI config for india project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'india' project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'india.settings')

# Get the WSGI application for Django
application = get_wsgi_application()

# Alias `application` to `app` for Vercel compatibility
app = application
