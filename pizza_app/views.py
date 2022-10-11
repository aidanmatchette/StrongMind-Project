from django.contrib.auth import authenticate, login, logout
from .models import AppUser
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def homepage(request):
    Index = open("build/index.html").read()
    return HttpResponse(Index)


@csrf_exempt
def log_in(request):
    data = json.loads(request.body)

    email = data["email"]
    password = data["password"]

    user = authenticate(username=email, password=password)

    if user is not None:
        if user.is_active:
            try:
                login(request, user)
                return JsonResponse(
                    {
                        "user": user.name,
                        "user_id": user.id,
                        "is_owner": user.is_owner,
                        "message": "You have successfully logged in",
                    },
                    status=200,
                )
            except Exception as e:
                return JsonResponse({"error message": e}, status=299)
        else:
            return JsonResponse(
                {"error message": "Your account is no longer active"}, status=299
            )
    else:
        return JsonResponse({"error message": "You do not have an account"}, status=299)


@csrf_exempt
def sign_up(request):
    data = json.loads(request.body)

    try:
        AppUser.objects.create_user(
            username=data["email"],
            password=data["password"],
            name=data["name"],
            email=data["email"],
            is_owner=data["is_owner"],
        )
        return JsonResponse(
            {"message": "Your account has been successfully created"}, status=200
        )
    except Exception as e:
        print(str(e))
        return JsonResponse(
            {"message": "There was an error during your request"}, status=299
        )


@csrf_exempt
def log_out(request):
    logout(request)
    return JsonResponse({"message": "You have successfully logged out"})
