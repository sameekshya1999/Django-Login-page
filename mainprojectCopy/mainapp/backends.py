from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class CustomFlagAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password) and user.is_active and getattr(user, 'flag', False):
            return user

        return None
