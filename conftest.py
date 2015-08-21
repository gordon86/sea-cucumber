from django.conf import settings


def pytest_configure():
    settings.configure(DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'simple_test_db'
        },

    })
