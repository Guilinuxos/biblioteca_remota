from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def mostrar_users(request):
    usuario = Usuario.objects.all()
    return render(request, "livros/index.html", {"usuario": usuario})

#LEITOR
def fazer_loginleitor(request):
    if request.method == "POST":
        cpf = request.POST["cpf"]
        email = request.POST["email"]
        senha = request.POST["senha"]

        try:
            usuario = Leitor.objects.get(
                cpf = cpf,
                email = email,
                senha = senha,
            )
            return redirect("tela_leitor")
        except Leitor.DoesNotExist:
            return render(request, "usuarios/login_leitor.html", {
                "erro": "falha no login"
            })
    return render(request, "usuarios/login_leitor.html")


#BIBLIOTECARIO
def fazer_loginbib(request):
    if request.method == "POST":
            cpf = request.POST["cpf"]
            email = request.POST["email"]
            senha = request.POST["senha"]
            matricula = request.POST["matricula"]
    
            try:
                bibliotecario = Bibliotecario.objects.get(
                    cpf = cpf,
                    email = email,
                    senha = senha,
                    matricula = matricula,
                )
                return redirect("tela_gestor")
            except Bibliotecario.DoesNotExist:
                return render(request, "usuarios/login_bib.html", {
                    "erro": "falha no login"
                })
    return render(request, "usuarios/login_bib.html")

def mostrar_leitores(request):
    bibliotecario = Bibliotecario.objects.first()

    leitores = bibliotecario.ver_leitores()

    return render(request, "usuarios/leitores.html", {
        "leitores": leitores
    })
