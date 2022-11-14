from django.urls import path
from .views import cadastro, login, sair, inicio

urlpatterns = [
    path('', inicio, name="inicio"),
    path('cadastro/', cadastro, name="cadastro"),
    path('login/', login, name="login"),
    path('sair/', sair, name="sair")
]