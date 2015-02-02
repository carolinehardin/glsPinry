import os

from django.contrib.messages import constants as messages


SITE_ROOT = os.path.join(os.path.realpath(os.path.dirname(__file__)), '../../')


# Set to False to disable people from creating new accounts.
ALLOW_NEW_REGISTRATIONS = True

# Set to False to force users to login before seeing any pins.
PUBLIC = True


TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = True


MEDIA_URL = '/media/'
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(SITE_ROOT, 'media')
STATIC_ROOT = os.path.join(SITE_ROOT, 'static')
TEMPLATE_DIRS = [os.path.join(SITE_ROOT, 'pinry/templates')]
STATICFILES_DIRS = [os.path.join(SITE_ROOT, 'pinry/static')]


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pinry.users.middleware.Public',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'pinry.core.context_processors.template_settings',
)
AUTHENTICATION_BACKENDS = (
    'pinry.users.auth.backends.CombinedAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
)


ROOT_URLCONF = 'pinry.urls'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
INTERNAL_IPS = ['127.0.0.1']
MESSAGE_TAGS = {
    messages.WARNING: 'alert alert-warning',
    messages.ERROR: 'alert alert-danger',
    messages.SUCCESS: 'alert alert-success',
    messages.INFO: 'alert alert-info',
}
API_LIMIT_PER_PAGE = 50


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'taggit',
    'compressor',
    'django_images',
    'pinry.core',
    'pinry.users',
)

IMAGE_PATH = 'pinry.core.utils.upload_path'
IMAGE_SIZES = {
    'thumbnail': {'size': [240, 0]},
    'standard': {'size': [600, 0]},
    'square': {'crop': True, 'size': [125, 125]},
}

SOUTH_MIGRATION_MODULES = {
    'taggit': 'taggit.south_migrations',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        # Include the default Django email handler for errors
        # This is what you'd get without configuring logging at all.
        'mail_admins': {
            'class': 'django.utils.log.AdminEmailHandler',
            'level': 'ERROR',
             # But the emails are plain text by default - HTML is nicer
            'include_html': True,
        },
        # Log to a text file that can be rotated by logrotate
        'logfile': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': 'pinry/static/error.log'
        },
    },
    'loggers': {
        # Again, default Django configuration to email unhandled exceptions
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propogate': True,
        },
        # Might as well log any errors anywhere else in Django
        'django': {
            'handlers': ['logfile'],
            'level': 'ERROR',
            'propogate': False,
        },
        # Your own app - this assumes all your logger names start with "myapp."
        'myapp': {
            'handlers': ['logfile'],
            'level': 'WARNING', # Or maybe INFO or DEBUG
            'propogate': False
        },
    },
    'file':
        {
            'level':
                'INFO',
            'class':
                'logging.FileHandler',
            'formatter':
                'verbose',
            'filename':
                'myapp.log'

        },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format':
                '%(levelname)s %(message)s'
        },
    },
}

ALLOWED_HOSTS = ['*']

FILE_UPLOAD_MAX_MEMORY_SIZE = 20971520
