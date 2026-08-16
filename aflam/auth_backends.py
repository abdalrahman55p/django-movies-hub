# aflam/auth_backends.py
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomAuthBackend(BaseBackend):
    """
    Backend يسمح بتسجيل الدخول باسم المستخدم فقط (بدون تحقق من كلمة المرور)
    أو بأي منطق مخصص.
    """
    def authenticate(self, request, username=None, password=None, **kwargs):
        if not username:
            return None

        user, created = User.objects.get_or_create(username=username)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
