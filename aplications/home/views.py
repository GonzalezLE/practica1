from django.shortcuts import render
from django.views.generic import TemplateView,ListView


class PruebaView(TemplateView):
  template_name = 'home/prueba.html'


class PurebaListView(ListView):    
  template_name = "home/lista.html"
  context_object_name='listaNumeros'
  queryset=['0','10','20','30','40','50']



