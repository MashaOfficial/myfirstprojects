"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.11.

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
SECRET_KEY = '5(o!35(qe4_mf7khc+@(xg+hj!shjp)^i4niwl(#uwnl(n=-f0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    # 'tinymce',
    # 'channels',
]

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'asgiref.inmemory.ChannelLayer',
        'ROUTING': 'myproj.routing.channel_routing',
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

LOGIN_REDIRECT_URL = '/'

# #TinyMCE widget configuration
# TINYMCE_JS_URL = STATIC_URL + "tiny_mce/tiny_mce.js"
# TINYMCE_JS_ROOT = STATIC_ROOT + "/tiny_mce"
# TINYMCE_SPELLCHECKER=False
# TINYMCE_PLUGINS = [
#     'safari',
#     'table',
#     'advlink',
#     'advimage',
#     'iespell',
#     'inlinepopups',
#     'media',
#     'searchreplace',
#     'contextmenu',
#     'paste',
#     'wordcount'
# ]

# TINYMCE_DEFAULT_CONFIG={
#     'theme' : "advanced",
#     'plugins' : ",".join(TINYMCE_PLUGINS), # django-cms
#     'language' : 'ru',
#     "theme_advanced_buttons1" : "bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,styleselect,formatselect,fontselect,fontsizeselect,|,spellchecker",
#     "theme_advanced_buttons2" : "cut,copy,paste,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,image,cleanup,code,|,forecolor,backcolor,|,insertfile,insertimage",
#     "theme_advanced_buttons3" : "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr",
#     'theme_advanced_toolbar_location' : "top",
#     'theme_advanced_toolbar_align' : "left",
#     'theme_advanced_statusbar_location' : "bottom",
#     'theme_advanced_resizing' : True,
#     'table_default_cellpadding': 2,
#     'table_default_cellspacing': 2,
#     'cleanup_on_startup' : False,
#     'cleanup' : False,
#     'paste_auto_cleanup_on_paste' : False,
#     'paste_block_drop' : False,
#     'paste_remove_spans' : False,
#     'paste_strip_class_attributes' : False,
#     'paste_retain_style_properties' : "",
#     'forced_root_block' : False,
#     'force_br_newlines' : False,
#     'force_p_newlines' : False,
#     'remove_linebreaks' : False,
#     'convert_newlines_to_brs' : False,
#     'inline_styles' : False,
#     'relative_urls' : False,
#     'formats' : {
#         'alignleft' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-left'},
#         'aligncenter' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-center'},
#         'alignright' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-right'},
#         'alignfull' : {'selector' : 'p,h1,h2,h3,h4,h5,h6,td,th,div,ul,ol,li,table,img', 'classes' : 'align-justify'},
#         'strikethrough' : {'inline' : 'del'},
#         'italic' : {'inline' : 'em'},
#         'bold' : {'inline' : 'strong'},
#         'underline' : {'inline' : 'u'}
#     },
#     'pagebreak_separator' : "",
#     # Drop lists for link/image/media/template dialogs
#     'template_external_list_url': 'lists/template_list.js',
#     'external_link_list_url': 'lists/link_list.js',
#     'external_image_list_url': 'lists/image_list.js',
#     'media_external_list_url': 'lists/media_list.js',
#     #
#     #'file_browser_callback':'tinyDjangoBrowser'
# }