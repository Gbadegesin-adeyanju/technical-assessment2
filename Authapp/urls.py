from django.urls import path, include
from .views import authenticationViewset, profileViewset, LoginViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', authenticationViewset, basename='authuser')
router.register(r'login/', LoginViewset, basename='login')
router.register(r'profile/', profileViewset, basename='profile')



urlpatterns = [
    path('', include(router.urls)),
]
