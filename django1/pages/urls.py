from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  # homepage for 0.0.0.0:8000
    path("about/", views.about, name="about"),
]
