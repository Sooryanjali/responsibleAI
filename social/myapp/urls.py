from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),  # Define a path for signup
    path("", views.signup, name="home"),  # Keep this if you want to route root to signup
    path("login/", views.login, name="login"),
]