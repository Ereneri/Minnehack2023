from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, "thegarden/index.html")
    # if request.user.is_authenticated:
    #     return render(request, "thegarden/index.html")
    # else:
    #     return render(request, "thegarden/login.html")


def login_view(request):
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
        pass
    else:
        return render(request, "thegarden/register.html")

def garden_view(request):
    return render(request, "thegarden/garden.html")

def tasks_view(request):
    pass
