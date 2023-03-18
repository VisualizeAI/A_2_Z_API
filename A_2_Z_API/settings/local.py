from .base import *
from decouple import config, Csv

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('LOCAL_DEBUG', cast=bool)

ALLOWED_HOSTS = config('LOCAL_ALLOWED_HOSTS', cast=Csv())

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': config('LOCAL_ENGINE'),
        'NAME': BASE_DIR / config('LOCAL_NAME'),
    }
}

# Celery settings
CELERY_BROKER_URL = config('LOCAL_CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = config('LOCAL_CELERY_RESULT_BACKEND')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'

# Email settings
EMAIL_BACKEND = config('LOCAL_EMAIL_BACKEND')
EMAIL_HOST = config('LOCAL_EMAIL_HOST')
EMAIL_PORT = config('LOCAL_EMAIL_PORT')
EMAIL_HOST_USER = config('LOCAL_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('LOCAL_EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True    # 587
EMAIL_USE_SSL = False   # 465

# S3 Bucket file upload settings
AWS_ACCESS_KEY_ID = config('DEV_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('DEV_AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('DEV_AWS_STORAGE_BUCKET_NAME')
DEFAULT_FILE_STORAGE = config('DEV_DEFAULT_FILE_STORAGE')
AWS_DEFAULT_ACL = config('DEV_AWS_DEFAULT_ACL')         						                    # ACL means Access Control List. by default inherits the bucket permissions.
AWS_S3_FILE_OVERWRITE = config('DEV_AWS_S3_FILE_OVERWRITE')  						                    # By default files with the same name will overwrite each other. True by default.
AWS_S3_REGION_NAME = config('DEV_AWS_S3_REGION_NAME')                                        #change to your region
AWS_S3_SIGNATURE_VERSION = config('DEV_AWS_S3_SIGNATURE_VERSION')
#STATICFILES_STORAGE = storages.backends.s3boto3.S3Boto3Storage                                     # To serve static file like css, js from AWS S3.
