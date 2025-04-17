from django.contrib.auth import views as auth_views
from django.urls import path
from myApp import views

urlpatterns = [
    # Redirect root URL to login page if not authenticated
    path('', auth_views.LoginView.as_view(template_name='custom_auth/login.html'), name='login'),
    
    # Other routes
    path('home/', views.home, name='home'),
    path('preferences/', views.preferences, name='preferences'),
    path('courses/', views.courses, name='courses'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
