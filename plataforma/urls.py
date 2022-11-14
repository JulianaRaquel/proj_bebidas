from django.urls import path
from .views import home, categoria, produto

urlpatterns = [
    path('home/', home, name='home'),
    path('categoria/<int:id>', categoria, name="categoria"),
    path('produto/<int:id>', produto, name="produto"),
]

