from django.urls import path, include
from .views import GoogleLogin
from allauth.socialaccount.providers.google.views import oauth2_login
from allauth import urls

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('auth/', include('rest_auth.urls')),
    path('auth/google/', GoogleLogin.as_view(), name='google_login'),
    # path('auth/google/callback/', google_callback, name='google_callback'),
    path('auth/google/url/', oauth2_login),
    path('auth/registration/', include('rest_auth.registration.urls')),
    
]
