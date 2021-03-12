from django.shortcuts import render
from django.views.generic import (
  TemplateView,
  ListView,
  CreateView)

from .models import Prueba

class PruebaView(TemplateView):
  template_name = 'home/prueba.html'


class PurebaListView(ListView):    
  template_name = "home/lista.html"
  context_object_name = 'listaNumeros'
  queryset=['0','10','20','30','40','50']

class ListaPrtueba(ListView):
  template_name = "home/lista_prueba.html"
  model = Prueba
  context_object_name='lista'

class pruebaCreateView(CreateView):
  template_name='home/add.html'
  model = Prueba
  fields = ['titulo','subtitulo','cantidad']


