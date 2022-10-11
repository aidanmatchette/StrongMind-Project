from django.urls import path
from .views import *


urlpatterns = [
    path("", homepage, name="homepage"),
    path("signup", sign_up, name="signup"),
    path("login", log_in, name="login"),
    path("logout/", log_out, name="logout"),
    path("whoami", who_am_i, name="whoami"),
]
