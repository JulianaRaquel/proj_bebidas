from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.messages import constants
import re

def cadastro(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/home')
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if len(senha) < 8:
            messages.add_message(request, constants.ERROR, 'Sua senha deve conter 8 ou mais caractertes')
            return redirect('/cadastro')

        elif not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem!')
            return redirect('/cadastro')

        elif not re.search('[A-Z]', senha):
            messages.add_message(request, constants.ERROR, 'Sua senha não contem letras maiúsculas')
            return redirect('/cadastro')

        elif not re.search('[a-z]', senha):
            messages.add_message(request, constants.ERROR, 'Sua senha não contem letras minúsculas')
            return redirect('/cadastro')

        elif not re.search('[1-9]', senha):
            messages.add_message(request, constants.ERROR, 'Sua senha não contém números')
            return redirect('/cadastro')

        """elif len(usuario).strip() == 0 or len(email).strip() == 0:
            messages.add_message(request, constants.ERROR, 'Usuário e senha não podem estar vazios')
            return redirect('/cadastro')"""

        try:
            usuario = User.objects.create_user(username=usuario, email=email, password=senha)
            usuario.save()

            messages.add_message(request, constants.SUCCESS, 'Cadastro realizado com sucesso !!!')
            return redirect('/cadastro')
        except:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/cadastro')


def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/home')
        return render(request, 'login.html')
    elif request.method == "POST":
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=usuario, password=senha)

        if not user:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
            return redirect('/login')
        else:
            # se o usuário existe no banco de dados, é feita a autenticação do mesmo
            auth.login(request, user)
            return redirect('/home')

def sair(request):
    auth.logout(request)
    return redirect('/login')

def inicio(request):
    return render(request, 'cadastro.html')

