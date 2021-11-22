from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from .views import *

urlpatterns = [
                  path('', about_page, name='about_page'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
