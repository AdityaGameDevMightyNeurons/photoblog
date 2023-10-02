from django.urls import path

from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("landscape/", views.Landscape, name="landscape"),
    path("specific/", views.Specific, name="specific"),
]