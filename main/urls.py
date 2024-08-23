from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("index", views.index, name = "index"),
    path("login", views.login, name = "login"),
    path("birthday/<str:name>", views.birthday, name = "birthday")

]
# Hello world abby
