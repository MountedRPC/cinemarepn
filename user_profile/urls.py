from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from user_profile.views import profile_user

urlpatterns = [
                  path('', profile_user, name='profile_user'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
