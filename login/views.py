from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def login(request):

    return HttpResponse ("this is my  <b> Login Page</b>")
