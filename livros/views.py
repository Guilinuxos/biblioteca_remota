from django.shortcuts import render
from django.http import HttpResponse
from .models import Livro

# Create your views here.
def index(request):
    livros = Livro.objects.all()
    return render(request, "livros/index.html", {"livros": livros})