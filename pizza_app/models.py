from django.db import models
from django.contrib.auth import AbstractUser


class AppUser(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    is_owner = models.BooleanField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Ingredients(models.Model):
    ingredient_name = models.CharField(max_length=255)

    def __str__(self):
        return self.ingredient_name


class Pizza(models.Model):
    pizza_name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Ingredients)

    def __str__(self):
        return self.pizza_name
