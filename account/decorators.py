# https://github.com/sibtc/django-multiple-user-types-example
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test, login_required
from LMS.constants import Student
from functools import wraps
from urllib.parse import urlparse
from django.conf import settings
from django.shortcuts import render, redirect


def role_required(function=None, role=Student):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                redirect('login')
            if not request.user.role == role:
                return redirect('login')
            if not request.user.is_email_verified:
                return redirect('account:verify_email')
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator