from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import CustomUserCreationForm
from .models import Account
from django.db import IntegrityError


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return render(request, "thegarden/index.html")
    else:
        return render(request, "thegarden/login.html")


def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if request.method == "POST":
            # Attempt to sign user in
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(request, email=email, password=password)

            # Check if authentication successful
            if user is not None:
                login(request, user)
                return render(request, "thegarden/index.html")
            else:
                return render(request, "thegarden/login.html", {
                    "message": "Invalid email and password."
                })
        else:
            return render(request, "thegarden/login.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        state = request.POST["state"]

        # Attempt to create new user
        try:
            user = Account.objects.create_user(email, username, state, password)
            user.save()
            login(request, user)
        except IntegrityError:
            return render(request, "thegarden/register.html", {
                "message": "Invalid username and/or email."
            })
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "thegarden/register.html")

def garden_view(request):
    return render(request, "thegarden/garden.html")

def tasks_view(request):
    pass

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect("/")