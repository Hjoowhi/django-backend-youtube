from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'password123')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get('DEBUG', 0)))

ALLOWED_HOSTS = ['*']


# Application definition

DJANGO_SYSTEM_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'common',
]

CUSTOM_USER_APPS = [
    'users.apps.UsersConfig', # Config : label 변경할 일이 많다.
    'videos.apps.VideosConfig',
    'comments.apps.CommentsConfig',
    'subscriptions.apps.SubscriptionsConfig',
    'reactions.apps.ReactionsConfig',
    'rest_framework',
    'drf_spectacular',
    'channels',
    'chat.apps.ChatConfig', # chat은 기능이라는 의미로 s를 따로 붙이지 않았다.
]

INSTALLED_APPS = DJANGO_SYSTEM_APPS + CUSTOM_USER_APPS

# Channels를 사용하기 위한 설정
ASGI_APPLICATION = 'app.route.application' # Socket (비동기처리) - 채팅 때 사용 + HTTP (동기)
# => FAST API (비동기) + (동기) : 기본적으로 비동기인데, 동기도 가능함
# chat 기능은 비동기로 처리할 예정

# 웹소켓 채팅 구현했습니다. => 웹소켓의 원리가 뭔가요?
# HTTP(단방향) 와 웹소켓(양방향)의 차이점은 뭐죠?
# HTTP - http://
# SOCKET - ws://, Hand Shake 향방향 통신이 가능해진다. Low Overhead(용량이 작아야 한다.), Frame(웹소켓에서 데이터를 나누는 단위)
# STREAMING - 영상 파일은 어떻게 보낼건지? TCP/UDP, 3 ways hand shake

WSGI_APPLICATION = 'app.wsgi.application' # HTTP Base - REST API (동기 처리)

# 동기와 비동기
# 스타벅스 입장했는데, 내 앞에 사람이 엄청난 옵션이 붙은 커스텀 음료를 시켰다.
# 근데 직원이 1명이야 (동기) -> 엄청난 커스텀 음료를 만들고, 그 다음 내 음료를 만드는 차례니깐
# 어라 직원이 2명이네 (비동기) -> 커스텀 음료 1명, 내 음료 1명 이렇게 만들 수 있음. 하지만 정확도가 떨어지는 이슈가 생길 수도 있다. -> 아아주세요 : 따뜻한 게 나왔는데요..?

# Worker => FAST API

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

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

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
    }
}


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django의 Custom UserModel - 기존 장고의 유저 인증 기능을 가져온다.
AUTH_USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer'
    }
}

STATIC_URL = '/static/static/'
MEDIA_URL = '/static/media/'

MEDIA_ROOT = '/vol/web/media'
STATIC_ROOT = '/vol/web/static'