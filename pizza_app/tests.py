from django.test import TestCase, Client
from .models import Pizza, Ingredients

client = Client()


class PizzaTestCase(TestCase):
    def setUp(self):
        return Pizza.objects.create(pizza_name="Pepperoni")

    def test_pizza_creation(self):
        pepperoni_pizza = self.setUp()

        self.assertTrue(isinstance(pepperoni_pizza, Pizza))


class IngredientsTestCase(TestCase):
    def setUp(self):
        return Ingredients.objects.create(ingredient_name="onion")

    def test_ingredient_creation(self):
        new_ingredient = self.setUp()

        self.assertTrue(isinstance(new_ingredient, Ingredients))


class URLTest(TestCase):
    def test_home_page(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
