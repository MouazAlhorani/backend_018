from django.urls import path, include
from .views import LoginViewSet
import app_018.views  as mV



urlpatterns = [
    path('', LoginViewSet.as_view({'get': 'fwlogin'})),
    path('api/login/', mV.LoginViewSet.as_view({'post': 'checklogin'})),
    path('api/logout/', mV.LoginViewSet.as_view({'post': 'logout'})),
]