import os  # isort:skip
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for AgencyTours project.
Python 2.7
Generated by 'django-admin startproject' using Django 1.11.20.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'oslc!8d2z83)ejb=y99t@!$4v1_hy29bf1-ypfctvk6mdp0od+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition





ROOT_URLCONF = 'AgencyTours.urls'




# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Lima'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'AgencyTours', 'static'),
)
SITE_ID = 1


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'AgencyTours', 'templates'),],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader'
            ],
        },
    },
]


MIDDLEWARE = [
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
]

INSTALLED_APPS = [
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'filer',
    'easy_thumbnails',
    'djangocms_column',
    'djangocms_file',
    # 'djangocms_link',
    # 'djangocms_picture',
    'djangocms_style',
    'djangocms_snippet',
    'djangocms_googlemap',
    'djangocms_video',

    'djangocms_icon',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_bootstrap4',
    'djangocms_bootstrap4.contrib.bootstrap4_alerts',
    'djangocms_bootstrap4.contrib.bootstrap4_badge',
    'djangocms_bootstrap4.contrib.bootstrap4_card',
    'djangocms_bootstrap4.contrib.bootstrap4_carousel',
    'djangocms_bootstrap4.contrib.bootstrap4_collapse',
    'djangocms_bootstrap4.contrib.bootstrap4_content',
    'djangocms_bootstrap4.contrib.bootstrap4_grid',
    'djangocms_bootstrap4.contrib.bootstrap4_jumbotron',
    'djangocms_bootstrap4.contrib.bootstrap4_link',
    'djangocms_bootstrap4.contrib.bootstrap4_listgroup',
    'djangocms_bootstrap4.contrib.bootstrap4_media',
    'djangocms_bootstrap4.contrib.bootstrap4_picture',
    'djangocms_bootstrap4.contrib.bootstrap4_tabs',
    'djangocms_bootstrap4.contrib.bootstrap4_utilities',

    'AgencyTours',
    'Data',
]

LANGUAGES = (
    ## Customize this
    ('en', gettext('en')),
    ('es', gettext('es')),
)

CMS_LANGUAGES = {
    ## Customize this
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'en',
            'hide_untranslated': False,
            'name': gettext('en'),
            'redirect_on_fallback': True,
        },
        {
            'public': True,
            'code': 'es',
            'hide_untranslated': False,
            'name': gettext('es'),
            'redirect_on_fallback': True,
        },
    ],
}

CMS_TEMPLATES = (
    ## Customize this
    ('home.html', 'Inicio'),
    ('day-tours.html', 'Day Tours'),
    ('adventure.html', 'Aventura'),
    ('trecking.html', 'Trecking'),
    ('contact.html', 'Contactar'),
    ('about.html', 'Nosotros'),

    ('fullwidth.html', 'Fullwidth'),
    ('sidebar_left.html', 'Sidebar Left'),
    ('sidebar_right.html', 'Sidebar Right')
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

""" DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': 'project.db',
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    }
}"""

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'DB_AgencyTours',
        'PASSWORD': 'postgres',
        'PORT': '5432',
        'USER': 'postgres'
    }
}

MIGRATION_MODULES = {
    
}

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters'
)

#-------------------------------------------------
#   New  configuration
#-------------------------------------------------

DJANGOCMS_STYLE_CHOICES = ['container', 'content', 'teaser', 'row']
DJANGOCMS_STYLE_TAGS = ['div', 'article', 'section', 'header', 'footer',
                        'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'i', 'li',
                        'span', 'strong']

#-------------------------------------------------
#   Bootstrap 4
#-------------------------------------------------
DJANGOCMS_BOOTSTRAP4_TAG_CHOICES = ['div', 'section', 'article', 'header', 'footer', 'aside']

DJANGOCMS_BOOTSTRAP4_CAROUSEL_TEMPLATES = (
    ('default', ('Default')),
)

DJANGOCMS_BOOTSTRAP4_GRID_SIZE = 12
DJANGOCMS_BOOTSTRAP4_GRID_CONTAINERS = (
    ('container', ('Container')),
    ('container-fluid', ('Fluid container')),
)
DJANGOCMS_BOOTSTRAP4_GRID_COLUMN_CHOICES = (
    ('col', ('Column')),
    ('w-100', ('Break')),
    ('', ('Empty'))
)

DJANGOCMS_BOOTSTRAP4_USE_ICONS = True

DJANGOCMS_BOOTSTRAP4_TAB_TEMPLATES = (
    ('default', ('Default')),
)

DJANGOCMS_BOOTSTRAP4_SPACER_SIZES = (
    ('0', '* 0'),
    ('1', '* .25'),
    ('2', '* .5'),
    ('3', '* 1'),
    ('4', '* 1.5'),
    ('5', '* 3'),
)

DJANGOCMS_BOOTSTRAP4_CAROUSEL_ASPECT_RATIOS = (
    (16, 9),
)

DJANGOCMS_BOOTSTRAP4_COLOR_STYLE_CHOICES = (
    ('primary', ('Primary')),
    ('secondary', ('Secondary')),
    ('success', ('Success')),
    ('danger', ('Danger')),
    ('warning', ('Warning')),
    ('info', ('Info')),
    ('light', ('Light')),
    ('dark', ('Dark')),
    ('custom', ('Custom')),
)
#-------------------------------------------------
#   Google Map
#-------------------------------------------------
DJANGOCMS_GMAPS_API_KEY = 'AIzaSyAUV1NLP4LxvrSuFxy99huU-VPchLi86aQ'

#-------------------------------------------------
#   Obs
#-------------------------------------------------
# import fa icon in base.html