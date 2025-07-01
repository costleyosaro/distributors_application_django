from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('theboss/', admin.site.urls),
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('Ghadco_PH(1)/', views.redirect_to_home, name="redirect_to_home"),  # ✅ Fixed path
    path('help/', views.help, name="help"),
    path('users/', include('Distributor_app.users.urls')),
    path("dashboard/", include("Distributor_app.dashboard.urls")),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
