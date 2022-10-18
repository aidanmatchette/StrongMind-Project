from django.urls import path
from .views import *


urlpatterns = [
    path("", homepage, name="homepage"),
    path("ingredients/", ingredients, name="ingredients"),
    path("ingredients/new", new_ingredient, name="new-ingredient"),
    path("ingredients/edit", edit_ingredients, name="edit-ingredients"),
    path("pizzas/", pizzas, name="pizzas"),
    path("pizzas/new", new_pizza, name="new-pizza"),
    path("pizzas/<int:pizza_id>/edit", edit_pizza, name="edit-pizza"),
]
