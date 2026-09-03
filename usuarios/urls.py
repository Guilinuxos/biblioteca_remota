from django.urls import path

from . import views

urlpatterns =  [
    path("", views.Leitor, name="mostrar_leitores")
]