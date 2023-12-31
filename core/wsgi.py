"""
WSGI config for core project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

# import os
# from django.core.wsgi import get_wsgi_application
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
# application = get_wsgi_application()

import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application
from . import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()
application = WhiteNoise(application, root=settings.STATIC_ROOT)
# application.add_files("/Users/bautistamateuci/Desktop/Support-Tickets-Manager/static", prefix="/")
