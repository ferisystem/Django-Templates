from django.contrib.auth.password_validation import validate_password
from django.test import TestCase
from django.conf import settings
# import os


class ConfigTest(TestCase):
    def test_secret_key_strengh(self):
        SECRET_KEY = settings.SECRET_KEY
        # SECRET_KEY = str(os.environ.get("DJANGO_SECRET_KEY"))
        try:
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            msg = f"Week secret key: {e.messages[0]}"
            self.fail(msg)