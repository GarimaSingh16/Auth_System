from django.urls import path
from .views import (
    home, login_view, dashboard_view, google_login,
    CustomTokenObtainPairView, UserProfileView , Register_View , google_profile , GoogleLogin
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),
    path('google-profile/', google_profile, name='google_profile'),
    path('', home, name='home'),  # Default home page
    path('login/', login_view, name='login'),  # Login page (Custom)
    path('dashboard/', dashboard_view, name='dashboard'),  # User dashboard
    path('google-login/', google_login, name='google_button'),  # Google OAuth login
    path('google-profile/', google_profile, name='google_profile'),  # Google Profile Page
    path('accounts/google/login/', GoogleLogin.as_view(), name='google_login'),

    # API Endpoints for Authentication
    path('api/register/', Register_View.as_view(), name='register'),  # API for user registration
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT Login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh JWT token
    path('api/user/', UserProfileView.as_view(), name='user_profile'),  # Get user profile
]


