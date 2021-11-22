from django.urls import path
from films.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', MoviesListView.as_view(), name='movies'),
                  path(r'films_<int:movies_id>/', details_films, name='details_films'),
                  path(r'films_<int:movies_id>/sessioninfo_<int:id_sess>/', sessionInfo, name='sessionInfo'),
                  path(r'films_<int:movies_id>/sessioninfo_<int:id_sess>/ticketbuy/', ticket_buy, name='ticketbuy')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
