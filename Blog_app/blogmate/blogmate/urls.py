from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', auth_views.LoginView.as_view(), name='login'),  # Login view as root
    path('blog/', include("blogmate_app.urls")),
    path('users/', include("users.urls")),
]

if settings.DEBUG:
    
    urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)