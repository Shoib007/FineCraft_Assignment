from django.urls import path
from .views import ProductView, ProductViewByIds

urlpatterns = [
    path('', ProductView.as_view()),
    path("<str:pk>/", ProductViewByIds.as_view()),
]