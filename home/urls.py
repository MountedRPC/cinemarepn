from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from home.views import *


urlpatterns = [
                  path('', Homepage, name='home'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
