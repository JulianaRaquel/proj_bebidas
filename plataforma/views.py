from django.shortcuts import render, redirect
from .models import Produto, Categoria
from django.contrib import messages
from django.contrib.messages import constants


def home(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            produtos = Produto.objects.all()
            categorias = Categoria.objects.all()
            return render(request, 'home.html', {'produtos': produtos, 'categorias': categorias})
        else:
            messages.add_message(request, constants.WARNING, 'Faça login para acessar a home')
            return redirect('/login')


def categoria(request, id):
    produtos = Produto.objects.filter(categoria_id=id)
    categorias = Categoria.objects.all()
    return render(request, 'home.html', {'produtos': produtos, 'categorias': categorias})

def produto(request, id):
    produto = Produto.objects.get(id=id)
    categorias = Categoria.objects.all()
    return render(request, 'produto.html', {'produto': produto, 'categorias': categorias})


