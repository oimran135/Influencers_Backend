from django.urls import path, include
from .views import (
    CustomTokenObtainPairView,
    InfluencerView,
    TestView,
    LogoutView,
    BrandAmbassadorView
)
urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    #path('social-auth/', include('djoser.social.urls')),
    path('test/', TestView.as_view()),
    path("logout/", LogoutView.as_view(), name="auth_logout"),
    path("auth/jwt/login/", CustomTokenObtainPairView.as_view(), name="auth_login"),
    path('influencer/all', InfluencerView.as_view(), name="all-influencers"),
    path('users/brand/ambassadors', BrandAmbassadorView.as_view()),
]
