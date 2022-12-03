from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home(requests: HttpRequest) -> HttpResponse:
    return render(requests, 'home.html')
