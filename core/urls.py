from django.urls import path
from . import views
urlpatterns = [
    path("", views.home,name="home" ),
    path("login/", views.Login, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("signup/", views.signup, name="signup")
    
]