from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('', TemplateView.as_view(template_name="index.html"), name="app")
]
