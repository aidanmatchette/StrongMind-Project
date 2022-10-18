from django.db import models


class Ingredients(models.Model):
    ingredient_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.ingredient_name


class Pizza(models.Model):
    pizza_name = models.CharField(max_length=255, unique=True)
    ingredients = models.ManyToManyField(Ingredients)

    def __str__(self):
        return self.pizza_name
