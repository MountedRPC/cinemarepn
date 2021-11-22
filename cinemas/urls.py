from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from cinemas.views import *

urlpatterns = [
                  path('', cinemas_view, name='cinemas'),
                  path('<int:cinem_id>/', detailcinemas, name='detailcinemas'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
