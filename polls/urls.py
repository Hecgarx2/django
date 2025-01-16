from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("saludo/<str:name>", views.greeting, name="saludo")
]