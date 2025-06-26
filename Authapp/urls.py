from django.urls import path, include
from .views import RegisterViewset, profileViewset, LoginView



urlpatterns = [
    path('register/', RegisterViewset.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', profileViewset.as_view(), name='profile'),
]
