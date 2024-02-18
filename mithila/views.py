from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.


def register(request):
    pass

def login(request):
    pass

def test(request):
    return JsonResponse({"data":"hello"})
