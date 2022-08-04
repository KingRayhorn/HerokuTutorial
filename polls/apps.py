from django.apps import AppConfig


class PollsConfig(AppConfig):
    INSTALLED_APPS = [
        'polls.apps.PollsConfig',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'polls',
    ]
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
