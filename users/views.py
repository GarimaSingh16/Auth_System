from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
import json
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import RegisterSerializer, CustomTokenObtainPairSerializer, UserProfileSerializer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class Register_View(APIView):
    def get(self, request):
        return render(request, "users/register.html")  # Show Register Page

    def post(self, request):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        return render(request, "users/register.html", {"error": "Invalid data"})



class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

def home(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':  # Handle AJAX Requests
        return JsonResponse({"message": "Welcome to the Authentication System"}, status=200)
    return render(request, "users/home.html")  # Render frontend template

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            if not email or not password:
                return JsonResponse({'error': 'Email and password are required'}, status=400)

            user = authenticate(username=email, password=password)

            if user is not None:
                login(request, user)
                refresh = RefreshToken.for_user(user)
                return JsonResponse({
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                    'message': 'Login successful!'
                }, status=200)
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=401)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    return render(request, 'users/login.html')  
    
class CustomTokenObtainPairView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')

            user = authenticate(username=email, password=password)

            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'access': str(refresh.access_token),
                    'refresh': str(refresh),
                    'message': 'Login successful!'
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        except json.JSONDecodeError:
            return Response({'error': 'Invalid JSON data'}, status=status.HTTP_400_BAD_REQUEST)

def dashboard_view(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"error": "Please log in first!"})
    return render(request, "users/dashboard.html", {"user": request.user})

@csrf_exempt
def google_login(request):
    if request.headers.get('Accept') == 'application/json':
        return JsonResponse({"login_url": "/accounts/google/login/"}, status=200)
    return render(request,"users/google_login.html")

def google_profile(request):
    user = request.user
    social_account = SocialAccount.objects.filter(user=user, provider='google').first()

    user_data = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'provider': 'Google',
        'profile_pic': social_account.extra_data.get('picture', '') if social_account else '',
    }

    if request.headers.get('Accept') == 'application/json':
        return JsonResponse({'message': 'Google Login Successful', 'user_data': user_data}, status=200)

    return render(request, 'google_profile.html', {'user': user_data})

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
