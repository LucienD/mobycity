# -*- coding: utf-8 -*-

"""
Django settings for mobycity project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

gettext = lambda s: s

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "c'est super secret"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [
    'localhost',
    'mobycity.net',
    'www.mobycity.net',
    'dev.mobycity.net',
]

LOGGING = {
    'version': 1,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers':['console'],
            'propagate': True,
            'level':'DEBUG',
        }
    },
}


# Application definition

INSTALLED_APPS = (
    'djangocms_admin_style', # for the admin skin. You **must** add 'djangocms_admin_style' in the list **before** 'django.contrib.admin'.

    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'cms',  # django CMS itself
    'mptt',  # utilities for implementing a tree
    'menus',  # helper for model independent hierarchical website navigation
    'sekizai',  # for javascript and css management
    'treebeard',
    
    'filer',
    'easy_thumbnails',

    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_link',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',

    'bootstrap3',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.twitter',
    'djangocms_text_ckeditor',
    'django_google_maps',
    'djangocms_ckeditor_filer',

    # MOBYCITY
    'cartography',
    'carpooling',
    'news',
    'contact',
    'user_profile',
)

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    
    # cms
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    
    'djangocms_ckeditor_filer.middleware.ThumbnailMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    
    # cms
    'sekizai.context_processors.sekizai',
    'cms.context_processors.cms_settings',
    
    # `allauth` specific context processors
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
)

ROOT_URLCONF = 'mobycity.urls'

WSGI_APPLICATION = 'mobycity.wsgi.application'

MIGRATION_MODULES = {
    'cmsplugin_filer_file': 'cmsplugin_filer_file.migrations_django',
    'cmsplugin_filer_folder': 'cmsplugin_filer_folder.migrations_django',
    'cmsplugin_filer_link': 'cmsplugin_filer_link.migrations_django',
    'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
    'cmsplugin_filer_teaser': 'cmsplugin_filer_teaser.migrations_django',
    'cmsplugin_filer_video': 'cmsplugin_filer_video.migrations_django',
}


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mobycity',
        'USER': 'mobycity',
        'PASSWORD': 'rub69vai06',
        'HOST': 'localhost',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'fr-fr'
USE_I18N = True

USE_L10N = True
TIME_ZONE = 'Europe/Paris'
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

TEMPLATE_DIRS = (
    # The docs say it should be absolute path: BASE_DIR is precisely one.
    # Life is wonderful!
    os.path.join(BASE_DIR, "templates"),
)

CMS_TEMPLATES = (
    ('mobycity/defaut.html', u'Défaut'),
    ('mobycity/accueil.html', 'Accueil'),
)

LANGUAGES = [
    ('fr-fr', u'Français'),
]

CMS_LANGUAGES = {
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [            
        {
            'public': True,
            'code': 'fr-fr',
            'hide_untranslated': False,
            'name': u'Français',
            'redirect_on_fallback': True,
        },
    ],
}

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

LOGIN_REDIRECT_URL = '/'
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {
            'auth_type': 'reauthenticate'
        },
        'METHOD': 'js_sdk',
        'LOCALE_FUNC': lambda request: 'fr_FR',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.3'
    }
}

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'

BOOTSTRAP3 = {
    # The URL to the jQuery JavaScript file
    'jquery_url': '//code.jquery.com/jquery.min.js',

    # The Bootstrap base URL
    'base_url': '//maxcdn.bootstrapcdn.com/bootstrap/3.3.5/',

    # The complete URL to the Bootstrap CSS file (None means derive it from base_url)
    'css_url': None,

    # The complete URL to the Bootstrap CSS file (None means no theme)
    'theme_url': None,

    # The complete URL to the Bootstrap JavaScript file (None means derive it from base_url)
    'javascript_url': None,

    # Put JavaScript in the HEAD section of the HTML document (only relevant if you use bootstrap3.html)
    'javascript_in_head': False,

    # Include jQuery with Bootstrap JavaScript (affects django-bootstrap3 template tags)
    'include_jquery': True,

    # Label class to use in horizontal forms
    'horizontal_label_class': 'col-md-3',

    # Field class to use in horizontal forms
    'horizontal_field_class': 'col-md-9',

    # Set HTML required attribute on required fields
    'set_required': True,

    # Set HTML disabled attribute on disabled fields
    'set_disabled': False,

    # Set placeholder attributes to label if no placeholder is provided
    'set_placeholder': True,

    # Class to indicate required (better to set this in your Django form)
    'required_css_class': '',

    # Class to indicate error (better to set this in your Django form)
    'error_css_class': 'has-error',

    # Class to indicate success, meaning the field has valid input (better to set this in your Django form)
    'success_css_class': 'has-success',

    # Renderers (only set these if you have studied the source and understand the inner workings)
    'formset_renderers': {
        'default': 'bootstrap3.renderers.FormsetRenderer',
    },
    'form_renderers': {
        'default': 'bootstrap3.renderers.FormRenderer',
    },
    'field_renderers': {
        'default': 'bootstrap3.renderers.FieldRenderer',
        'inline': 'bootstrap3.renderers.InlineFieldRenderer',
    },
}

CKEDITOR_SETTINGS = {
    'language': 'fr',
    'contentsCss': [
        STATIC_URL + 'mobycity/stylesheets/screen.css',
    ],
    'toolbar_CMS': [
        ['Undo', 'Redo'],
        ['cmsplugins','-','ShowBlocks'],
        ['Format','Styles'],
        ['Maximize'],
        [ 'Cut','Copy','Paste','PasteText','PasteFromWord','-','Undo','Redo' ],
        [ 'Bold','Italic','Underline','Strike','Subscript','Superscript','-','RemoveFormat' ],
        [ 'NumberedList','BulletedList','-','Outdent','Indent','-','Blockquote','CreateDiv','-','JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],
        [ 'Link','Unlink','Anchor' ],
        [ 'Filer Image','Image','Flash','Table','HorizontalRule','Smiley','SpecialChar','PageBreak','Iframe' ],
        [ 'Source' ],
    ],
    'stylesSet': [
        { 'name': 'Mise en exergue', 'element': 'em' },
        { 'name': 'Bloc titre', 'element': 'div', 'attributes': { 'class': 'bloc-titre' } },
        { 'name': 'Bloc 1 colonne', 'element': 'div', 'attributes': { 'class': 'colonnes-1' } },
        { 'name': 'Bloc 2 colonnes', 'element': 'div', 'attributes': { 'class': 'colonnes-2' } },
        { 'name': 'Bloc de partenaires', 'element': 'div', 'attributes': { 'class': 'partenaires' } },
    ],
    'extraPlugins': 'filerimage',
    'removePlugins': 'image',
}

TEXT_SAVE_IMAGE_FUNCTION = 'cmsplugin_filer_image.integrations.ckeditor.create_image_plugin'

THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    #'easy_thumbnails.processors.scale_and_crop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mobycityplateforme@gmail.com'
EMAIL_HOST_PASSWORD = 'rub69vai06'
DEFAULT_FROM_EMAIL = 'mobycityplateforme@gmail.com'
#DEFAULT_TO_EMAIL = 'mobycityplateforme@gmail.com'

ADMINS = [('Mobycity', 'mobycityplateforme@gmail.com')]
MANAGERS = ADMINS

TEST_RUNNER = 'django.test.runner.DiscoverRunner'
