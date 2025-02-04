from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('changepass/', views.UserchangePass.as_view(), name='change_pass'),
    path('send-password-reset-email/', views.PassResetPassEmailView.as_view(), name='send_password_reset_email'), 
    path('reset-email/<uid>/<token>/', views.UserPasswordResetView.as_view(), name='reset_email'), 

 

]
