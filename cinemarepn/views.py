from django.shortcuts import render
from django.contrib.auth.models import User


def page_not_found_view(request, exception):
    return render(request, 'error404/404.html', status=404)
