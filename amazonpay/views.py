from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def payments(request):
    return HttpResponse('<h1>payments will be done here</h1>')