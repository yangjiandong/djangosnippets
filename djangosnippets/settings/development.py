#!/usr/bin/envs python
#-*- coding: utf-8 -*-#
from djangosnippets.settings.base import *

DEBUG = True

TIME_ZONE = 'Asia/Shanghai'
LANGUAGE_CODE = 'zh-cn'

SECRET_KEY = 'abcdefghijklmnopqrstuvwxyz0123456789'

STATIC_URL = '/assets/static/'

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

#django-debug-toolbar
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INSTALLED_APPS += ('debug_toolbar',)
INTERNAL_IPS = ['127.0.0.1']
DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}