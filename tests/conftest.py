import django
from django.conf import settings

def pytest_configure():
    settings.configure(
        SECRET_KEY='secret_key',
        INSTALLED_APPS=(
            'django.contrib.staticfiles',
            'django_google_charts',
        ),
        STATIC_URL='/static/'
    )
    django.setup()
