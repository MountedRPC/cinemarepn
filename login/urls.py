from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from login.views import *

urlpatterns = [
                  path('login/', login_people, name='login'),
                  path('registation/', registation, name='registation'),
                  path('exit/', custom_logout, name='exit'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
