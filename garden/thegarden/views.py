from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, "thegarden/index.html")


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponse("Logged in")
        else:
            return render(request, "thegarden/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "thegarden/login.html")

def register_view(request):
    if request.method == "POST":
        pass
    else:
        return render(request, "thegarden/register.html")

def garden_view(request):
    return render(request, "thegarden/garden.html")

def tasks_view(request):
    pass
