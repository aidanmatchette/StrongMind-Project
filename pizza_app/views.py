from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, reverse
from .models import Ingredients, Pizza


def homepage(request):
    return render(request, "pages/index.html")


def ingredients(request):
    data = {}
    data["ingredients"] = Ingredients.objects.all()
    return render(request, "pages/ingredients.html", data)


def new_ingredient(request):
    data = {}

    if request.method == "POST":
        try:
            ingredient = Ingredients()
            ingredient.ingredient_name = request.POST["name"]
            ingredient.full_clean()
            ingredient.save()

            return redirect("ingredients")

        except ValidationError as ve:
            data["error"] = ve.message_dict

    return render(request, "pages/new_ingredient.html", data)


def edit_ingredients(request):
    data = {}
    data["ingredients"] = Ingredients.objects.all()

    if request.method == "POST":
        delete_record = "delete" in request.POST

        try:
            if delete_record:
                record_id = request.POST["delete"]
                Ingredients.objects.get(pk=record_id).delete()
            else:
                update_id = request.POST["add"]
                update_record = Ingredients.objects.get(pk=update_id)
                update_record.ingredient_name = request.POST["ingredient_name"]
                update_record.full_clean()
                update_record.save()

            return redirect("ingredients")
        except ValidationError as ve:
            data["error"] = ve.message_dict

    return render(request, "pages/edit_ingredients.html", data)


def pizzas(request):
    data = {}
    data["pizzas"] = Pizza.objects.all()

    if request.method == "POST":
        delete_record = "delete" in request.POST
        try:
            if delete_record:
                record_id = request.POST["delete"]
                Pizza.objects.get(pk=record_id).delete()
            return redirect("pizzas")

        except ValidationError as ve:
            data["error"] = ve.message_dict

    return render(request, "pages/pizzas.html", data)


def new_pizza(request):
    data = {}
    data["ingredients"] = Ingredients.objects.all()

    if request.method == "POST":
        try:
            pizza = Pizza()
            pizza.pizza_name = request.POST["name"]
            pizza.save()

            for ingredient in request.POST.getlist("ingredients"):
                pizza.ingredients.add(Ingredients.objects.get(id=ingredient))

            pizza.full_clean()
            pizza.save()

            return redirect("pizzas")

        except ValidationError as ve:
            data["error"] = ve.message_dict

    return render(request, "pages/new_pizza.html", data)


def edit_pizza(request, pizza_id):
    data = {}
    data["pizza"] = Pizza.objects.get(pk=pizza_id)
    data["ingredients"] = Ingredients.objects.all()

    if request.method == "POST":
        print("ddddddddd", request.POST)
        delete_record = "delete" in request.POST
        delete_ingredient = "delete_ingredient" in request.POST
        update_name = "pizza_name" in request.POST

        try:
            if delete_record:
                record_id = request.POST["delete"]
                Pizza.objects.get(pk=record_id).delete()

                return redirect("pizzas")
            elif delete_ingredient:
                ingredient_id = request.POST["delete_ingredient"]
                curr_pizza = Pizza.objects.get(pk=pizza_id)
                curr_pizza.ingredients.remove(Ingredients.objects.get(id=ingredient_id))
            elif update_name:
                curr_pizza = Pizza.objects.get(pk=pizza_id)
                curr_pizza.pizza_name = request.POST["pizza_name"]

                curr_pizza.full_clean()
                curr_pizza.save()

            else:
                new_ingredient = request.POST["new_ingredient"]
                curr_pizza = Pizza.objects.get(pk=pizza_id)
                curr_pizza.ingredients.add(Ingredients.objects.get(id=new_ingredient))

                curr_pizza.full_clean()
                curr_pizza.save()

            return redirect(reverse("edit-pizza", args=(pizza_id,)))
        except ValidationError as ve:
            data["error"] = ve.message_dict

    return render(request, "pages/edit_pizzas.html", data)
