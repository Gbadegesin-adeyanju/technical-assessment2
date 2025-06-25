from django.urls import path, include
from .views import authenticationViewset, profileViewset, LoginView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'authapp/', authenticationViewset, basename='authuser')
router.register(r'profile/', profileViewset, basename='profile')



urlpatterns = [
    path('', include(router.urls)), 
    path('login/', LoginView.as_view(), name='login'),
]
