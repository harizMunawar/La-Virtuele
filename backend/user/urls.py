from django.urls import path, include
from rest_framework_simplejwt.views import TokenVerifyView
from . import views

app_name = 'user'

urlpatterns = [
    path('', include('djoser.urls')),
    path('jwt/create/', views.VirtueleTokenObtainPairView.as_view()),
    path('jwt/refresh/', views.VirtueleTokenRefreshView.as_view()),
    path('jwt/verify/', TokenVerifyView.as_view())
]