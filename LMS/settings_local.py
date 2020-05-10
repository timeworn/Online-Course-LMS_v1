import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG = True
ALLOWED_HOSTS = ['192.168.208.75', 'localhost', '127.0.0.1']
STATIC_URL = '/assets/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "assets"),
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'upload')
MEDIA_URL = '/media/'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# Usedin Activation Email Code Geneartor 
DOMAIN = '127.0.0.1:8000'
