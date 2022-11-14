from django.db import models
from django.utils.safestring import mark_safe

class Categoria(models.Model):
    categoria = models.CharField(max_length=30)

    def __str__(self):
        return self.categoria

class Produto(models.Model):
    nome = models.CharField(max_length=30)
    img = models.ImageField(upload_to='post_img')
    preco = models.FloatField()
    descricao = models.TextField()
    ingredientes = models.TextField(default='blank')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)

    @mark_safe
    def icone(self):
        return f'<img width="30px" src="/media/{self.img}">'

    def __str__(self):
        return self.nome

