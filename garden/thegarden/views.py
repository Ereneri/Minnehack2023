from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import CustomUserCreationForm
from .models import Account


# Create your views here.
def index(request):
    return render(request, "thegarden/index.html")
    # if request.user.is_authenticated:
    #     return render(request, "thegarden/index.html")
    # else:
    #     return render(request, "thegarden/login.html")


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
                return HttpResponse("logging in")
            else:
                return HttpResponse("fuck")
        else:
            return render(request, "thegarden/login.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        # Attempt to create new user
        user = Account.objects.create_user(username, email, password)
        user.save()
        login(request, user)
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