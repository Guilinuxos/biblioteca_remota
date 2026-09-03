from django.shortcuts import render
from django.http import HttpResponse
from .models import Livro

# Create your views here.
def mostrar_livros(request):
    livros = Livro.objects.all()
    return render(request, "livros/acervo.html", {"livros": livros})
