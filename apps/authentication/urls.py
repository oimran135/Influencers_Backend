from django.urls import path, include
from .views import CustomTokenObtainPairView
from .views import TestView, LogoutView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('test/', TestView.as_view()),
    path("logout/", LogoutView.as_view(), name="auth_logout"),
    path("auth/jwt/login/", CustomTokenObtainPairView.as_view(), name="auth_login")
]
