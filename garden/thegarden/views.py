from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import CustomUserCreationForm
from .models import Account, Task
from django.db import IntegrityError
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers

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
    return render(request, "thegarden/index.html")


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect("/")

@login_required
def list(request):
    user = request.user
    # Return list contents
    if request.method == "GET":
        items = Task.objects.filter(user=user)
        if (items.count() == 0):
            return JsonResponse({'error':'No Tasks'}, safe=False)
        items = items.all()
        return JsonResponse([item.serialize() for item in items], safe=False)

    # task must be via GET or PUT
    else:
        return JsonResponse({
            "error": "GET or PUT request required."
        }, status=400)

@login_required
def list_view(request):
    return render(request, "thegarden/list.html")
