from django.urls import path
from pokeapp import views

urlpatterns=[
    path("", views.index),
    path("pokelist", views.pokelist, name="pokelist"),
    path("typelist", views.typelist, name="typelist"),
    path("add_pokemon", views.add_pokemon_form, name="add_pokemon"),
    path ("add_type", views.add_type_form, name="add_type")
]