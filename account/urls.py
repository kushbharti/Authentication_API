from django.urls import path
from account.views import UserRegistrationView,UserLoginView,UserProfileView,UserChangePasswordView,SendPasswordResetEmailView,UserPasswordResetView

urlpatterns = [
   path('register/',UserRegistrationView.as_view(),name='register'),
   path('login/',UserLoginView.as_view(),name='login'),
   path('user-profile/',UserProfileView.as_view(),name='user-profile'),
   path('change-password/',UserChangePasswordView.as_view(),name='change-password'),
   path('send-reset-password-email/',SendPasswordResetEmailView.as_view(),name='send-reset-password-email'),
   path('reset-password/<uid>/<token>/',UserPasswordResetView.as_view(),name='reset-password'),
]
