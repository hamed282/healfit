from pathlib import Path
from datetime import timedelta
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o9+xpypiz1b)!21(fh*kmzbl2uff7_8e@38mc6cb^fk2^=q4zs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
    ALLOWED_HOSTS = ['*']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.mysql',
    #         'NAME': 'healfita_healfit',
    #         'USER': 'healfita_healfit_user',
    #         'PASSWORD': 'BE*]ZjDOk^Tj',
    #         'HOST': 'localhost',
    #         'PORT': '3306',
    #     }
    # }

    STATIC_ROOT = "staticfiles"
    STATIC_URL = 'static/'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static/'),
    )

else:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'rest.healfit.ae', 'www.rest.healfit.ae'] #https://healfit.ae
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'healfita_healfit',
            'USER': 'healfita_healfit_user',
            'PASSWORD': 'BE*]ZjDOk^Tj',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }

    STATIC_URL = 'static/'
    STATIC_ROOT = "staticfiles"
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static/'),
    )

    CSRF_TRUSTED_ORIGINS = ['https://*.rest.healfit.ae', 'https://*.127.0.0.1']

CORS_ORIGIN_ALLOW_ALL = True

# Application definition

INSTALLED_APPS = [
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    "whitenoise.runserver_nostatic",
    'django.contrib.staticfiles',
    'drf_spectacular',
    'corsheaders',
    'rest_framework_simplejwt.token_blacklist',
    'django_rest_passwordreset',

    # Install app   
    'accounts.apps.AccountsConfig',
    'home.apps.HomeConfig',
    'order.apps.OrderConfig',
    'product.apps.ProductConfig',
    'user_panel.apps.UserPanelConfig',
    'django_celery_beat',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = 'A.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates/'],
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

WSGI_APPLICATION = 'A.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dubai'

USE_I18N = True

USE_TZ = True

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'accounts.User'

REST_FRAMEWORK = {

    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

# CSRF_COOKIE_HTTPONLY = False
# SESSION_COOKIE_HTTPONLY = False
# CORS_ALLOW_CREDENTIALS = True
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SAMESITE = 'None'
# SESSION_COOKIE_SAMESITE = 'None'
#
# CORS_EXPOSE_HEADERS = ["Set-Cookie"]

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=90),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=180),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(days=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}


CART_SESSION_ID = 'cart'

# STORAGES = {
#     # ...
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }

# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True
#
# INTERNAL_IPS = ['127.0.0.1', '::1', '0.0.0.0']


# TELR Settings
TELR_API_REQUEST = f"https://secure.telr.com/gateway/order.json"
TELR_API_VERIFY = f"https://secure.telr.com/gateway/order.json"
TEST = "1"
FRAMED = 0
SOTRE_ID = 29934
AUTHKEY = 'BnCdX#DGW2P@HHxk'
CURRENCY = "AED"
AUTHORIZED_URL = "https://healfit.ae/success-pay"  # "https://rest.healfit.ae/api/order/authorised/"
DECLINED_URL = "https://healfit.ae/unsuccess-pay"  # "https://rest.healfit.ae/api/order/declined/"
CANCELLED_URL = "https://healfit.ae/cancel-pay-pay"  # "https://rest.healfit.ae/api/order/cancelled/"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.healfit.ae'
EMAIL_HOST_USER = 'no-reply@healfit.ae'
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = 'Ljho,cP4tD#@'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_USE_TLS = False

# Zoho Config
ORGANIZATION_ID = '846612922'
CLIENT_ID = '1000.4BT978BGTIN610OF1XIJQAQKACB7WY'
CLIENT_SECRET = '2f9c6b2ec7a303bda3f7aa12081a0b34996073ff23'
GRANT_TYPE = 'client_credentials'
SCOPE_READING = 'ZohoInventory.items.READ'
SCOPE_UPDATE = 'ZohoInventory.items.UPDATE'
SCOPE_BOOK_CONTACTS = 'ZohoBooks.contacts.CREATE'
SCOPE_BOOK_INVOICE = 'ZohoBooks.invoices.CREATE'
SCOPE_BOOK_TAX = 'ZohoBooks.settings.READ'
SIOD = f'ZohoInventory.{ORGANIZATION_ID}'
