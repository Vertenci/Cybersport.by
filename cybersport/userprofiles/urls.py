from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.profile_home, name='profile'),
    path('login/', views.pre_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('verify-email/', views.verify_email, name='verify_email'),
    path('resend_verification_code/', views.resend_verification_code, name='resend_verification_code'),
]