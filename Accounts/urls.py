from django.urls import path
from .views import HomeView, UserRegistrationsView, UserLoginLogoutView

urlpatterns = [
    path('', HomeView.as_view()),
    path('register/', UserRegistrationsView.as_view()),
    path('auth/', UserLoginLogoutView.as_view()),
]