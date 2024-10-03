from django.conf import settings
from django.http import HttpResponse
from django import get_version
import platform

def get_toy_info():
    # Get Django version
    django_version = get_version()

    # Get Python version
    python_version = platform.python_version()

    # Display Django and Python versions
    return HttpResponse(f"Django Version: {django_version} Python Version: {python_version}")