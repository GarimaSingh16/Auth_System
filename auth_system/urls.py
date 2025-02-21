from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('accounts/', include('allauth.urls')),  # Google OAuth authentication
    path('api/auth/', include('rest_framework.urls')),  # Django Rest Framework built-in auth views
    path('', include('users.urls')),  # Include user-related API endpoints
]
