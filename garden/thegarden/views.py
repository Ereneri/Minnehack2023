from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import CustomUserCreationForm
from .models import Account, Score, Task
from django.db import IntegrityError
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, "thegarden/index.html", {
            "score": Score.objects.filter(user=user).first().score,
        })
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
            print(email + password)

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
    if request.user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        if request.method == "POST":
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]
            state = request.POST["state"]

            # Attempt to create new user
            try:
                user = Account.objects.create_user(email, username, state, password)
                listofitems = [
                    "Volunteered or participated in community service",
                    "Shoveled or mowed for a neighbor",
                    "Baby or dog sat for a neighbor",
                    "Visited a nursing home",
                    "Send cards to soldiers/elderly",
                    "Volunteer at a church or social event",
                    "Donated non perishable food to a charity drive",
                    "Donated money to charity",
                    "Donated supplies to a local nonprofit",
                    "Planted a tree or plant",
                    "Cleaned up trash at a local park",
                    "Used public transportation or a carpool",
                    "Adopted a pet from an animal shelter",
                    "Attended a community gathering",
                    "Started a community social group",
                    "Met a new neighbor",
                    "Help someone register to vote"
                ]
                for item in listofitems:
                    task = Task(user=user, title=item)
                    task.save()
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
