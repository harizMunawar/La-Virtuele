from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView
from django.urls import reverse
from django.shortcuts import redirect
import urllib.parse


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client

# def google_callback(request):
#     params = urllib.parse.urlencode(request.GET)
#     return redirect(f'http://127.0.0.1:8000/accounts/profile/?{params}')