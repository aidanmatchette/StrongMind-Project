from django.contrib import admin
from .models import Ingredients, Pizza


admin.site.register([Ingredients, Pizza])
