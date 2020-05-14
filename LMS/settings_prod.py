import os
#DEBUG = False
ALLOWED_HOSTS = ['103.100.62.146']
STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/html/BookApp/static'
MEDIA_ROOT = '/var/www/html/BookApp/upload'
MEDIA_URL = '/media/'

print("Debug Flase")
DOMAIN = 'online-lms.herokuapp.com'

SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY', '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')

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True
