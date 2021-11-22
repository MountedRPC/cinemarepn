from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path

urlpatterns = [
                  path('', include('home.urls'), name='homepage'),
                  path('cinemas/', include('cinemas.urls'), name='cinemas'),
                  path('movies/', include('films.urls'), name='movies'),
                  path('accounts/', include('login.urls'), name='login'),
                  path('profile/', include('user_profile.urls'), name='profile'),
                  path('about/', include('about.urls'), name='about_page'),
                  path('admin/', admin.site.urls),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
handler404 = "cinemarepn.views.page_not_found_view"
