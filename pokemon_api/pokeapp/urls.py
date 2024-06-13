from django.urls import path
from pokeapp import views

urlpatterns=[
    path("", views.index)
]