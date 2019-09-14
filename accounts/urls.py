from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginView, name="login_url"),
    path('register/', views.registerView, name="register_url"),
    path('logout/', views.logoutView, name="logout_url"),
]