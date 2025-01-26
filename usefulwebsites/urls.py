from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('', include('websites.urls')),  # Main app's URL patterns
    path('accounts/', include('django.contrib.auth.urls')),  # Authentication (login, logout, etc.)
]


