#!/usr/bin/envs python
#-*- coding: utf-8 -*-#
from djangosnippets.settings.base import *

TIME_ZONE = 'Asia/Shanghai'
LANGUAGE_CODE = 'zh-cn'

SECRET_KEY = 'abcdefghijklmnopqrstuvwxyz0123456789'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'assets', 'static')
STATIC_URL = '/assets/static/'
ADMIN_MEDIA_PREFIX = '/assets/static/admin/'

ADMINS = (
)
MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(PROJECT_ROOT, "snippets.db"),
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#虚拟缓存
CACHE_BACKEND = 'dummy://'

HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_WHOOSH_PATH = os.path.join(PROJECT_ROOT, 'whoosh_index')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}
