from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from rest_framework import exceptions

User = get_user_model()


class CustomBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        username = kwargs['username']
        confirmation_code = kwargs['confirmation_code']
        try:
            user = User.objects.get(username=username)
            if not user.confirmation_code == confirmation_code:
                raise exceptions.ParseError('Confirmation code не совпадает')
            return user
        except User.DoesNotExist:
            pass
