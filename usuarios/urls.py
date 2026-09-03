from django.urls import path

from . import views

urlpatterns =  [
    path("login/", views.fazer_login, name="fazer_login"),
    path("cadastrar/", views.cadastrar_livro, name="cadastrar_livro"),
]