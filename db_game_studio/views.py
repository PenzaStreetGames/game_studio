from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.


def index(request: HttpRequest):
    is_login = request.user.is_authenticated
    return render(
        request,
        "index.html",
        context={
            "is_login": is_login
        }
    )


def login():
    pass


def logout():
    pass


def profile():
    pass


def get_task_list():
    pass


def get_task():
    pass


def create_task():
    pass


def update_task():
    pass


def get_version_list():
    pass


def get_version():
    pass


def create_version():
    pass
