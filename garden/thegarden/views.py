from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, "thegarden/index.html")


def login_view(request):
    if request.method == "POST":
        pass
    else:
        return render(request, "thegarden/login.html")
