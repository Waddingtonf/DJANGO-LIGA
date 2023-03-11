from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
# Create your views here.

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def docad(request):
    # Realizar Cadastro
    data = {}

    tabela = User.objects.all()

    if request.method == 'POST':
        if request.POST['usuario'] is None:
            data['msg'] = 'Campo Usuário Vazio'
            return render(request,'cadastro.html', data)

        user = User.objects.create_user(request.POST['usuario'], request.POST['senha'])
        user.save()
        data['msg'] = 'Usuário Cadastrado com Sucesso!'
        return render(request,'cadastro.html', data)

    return render(request,'cadastro.html', data)

def dologin(request):
    data = {}
    user = authenticate(username=request.POST['usuario'], password = request.POST['senha'])
    if user is not None:
        login(request, user)
        return render(request, 'inscritos.html')
    else:
        data['msg'] = 'Usuário ou Senha Incorreta!'
    return render(request, 'login.html', data)

def inscritos(request):
    return render(request, 'inscritos.html')