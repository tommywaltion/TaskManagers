from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.login_view, name="login"),
    path('register/', views.register_view, name='register'),
    path('landing/', views.landing_page, name='landing'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('about/', views.about_page, name='about'),
]