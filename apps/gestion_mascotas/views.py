from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def log(request):
    log_in = "Login"
    return HttpResponse(log_in)

def principal(request):
    data = [1,5,9,3,10,100]
    return HttpResponse(str(data))

