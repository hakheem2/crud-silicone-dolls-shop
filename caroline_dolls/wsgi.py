"""
WSGI config for caroline_dolls project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'caroline_dolls.settings')

application = get_wsgi_application()


import django
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

django.setup()

User = get_user_model()

try:
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='hakheem',
            email='hakheemwyatt2@gmail.com',
            password='holli123.J'  # 👈 Change this to a secure password
        )
        print("Superuser created successfully!")
except IntegrityError:
    print("Superuser already exists.")
