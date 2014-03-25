# coding: utf-8
# Environment-specific settings

DEBUG = True
ENVIRONMENT = 'DEV' #change to DEV in your machine
DATABASE_NAME = 'frespo'
DATABASE_USER= 'frespo'
DATABASE_PASS = 'frespo'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


AUTO_EMAIL_USERNAME = 'noreply@freedomsponsors.com'
AUTO_EMAIL_PASSWORD = 'ThisIsNotTheRealPassword_obviously'

SITE_HOST = 'localhost:8000' # www.freedomsponsors.org
SITE_NAME = 'FreedomSponsors_test' # FreedomSponsors
PAYPAL_USE_SANDBOX = True
BITCOIN_IPNNOTIFY_URL_TOKEN = 'secretipn'
BITCOIN_ENABLED = True
