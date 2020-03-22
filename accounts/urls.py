from django.urls import path, include
from django.contrib.auth import views
from django.contrib.auth import views
from accounts import views as accounts_views


urlpatterns = [
    path('register/', accounts_views.register, name='user-register'),
    path('profile/', accounts_views.profile, name='user-profile'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='user-login'),
    path('logout/', views.LogoutView.as_view(template_name='logout.html'), name='user-logout'),
    path('reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/complete/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
