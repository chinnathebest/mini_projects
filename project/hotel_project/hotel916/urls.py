from django.urls import path
from . import views

urlpatterns=[
    path('mainpage/',views.index, name="index"),
    path('register/',views.register),
    path('login/',views.login),
]