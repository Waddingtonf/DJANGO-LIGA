from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def home(requests):
    return render(requests, 'home.html')

def login(requests):
    return render(requests, 'login.html')

def inscritos(requests):
    return render(requests, 'inscritos.html')