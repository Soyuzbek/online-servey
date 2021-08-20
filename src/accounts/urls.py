from django.urls import path
from accounts import views

urlpatterns = [
    path('login', views.LoginAPIView.as_view(), name='login'),
    path('logout', views.LogoutAPIView.as_view(), name='logout'),
    path('register', views.RegisterAPIView.as_view(), name='register')
]
