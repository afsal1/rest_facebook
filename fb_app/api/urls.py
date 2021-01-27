from django.urls import path
from .views import SocialLoginView

app_name = 'fb_app'

urlpatterns = [
    path('oauth/login/', SocialLoginView.as_view()),
]