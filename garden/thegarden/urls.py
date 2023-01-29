from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("garden/", views.garden_view, name="garden"),
    path("logout/", views.logout_view, name="logout"),
    path("list_data/", views.list, name="list"),
    path("list/", views.list_view, name="list_view"),
]