# aflam/middleware/auto_login.py
from django.conf import settings
from django.contrib.auth import get_user_model, login
from django.utils.deprecation import MiddlewareMixin

class AutoLoginMiddleware(MiddlewareMixin):
    """
    Middleware for development only.
    If DEBUG True and request.user not authenticated -> logs in a given user.
    """
    def process_request(self, request):
        if not settings.DEBUG:
            return None

        if request.user.is_authenticated:
            return None

        User = get_user_model()
        try:
            user = User.objects.get(username="admin")  # غيّر اسم المستخدم حسب الموجود عندك
        except User.DoesNotExist:
            return None

        # لازم تُعيّن backend قبل login() إذا لم يكن موجودًا
        user.backend = "django.contrib.auth.backends.ModelBackend"
        login(request, user)
        return None
