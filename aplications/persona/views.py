from django.shortcuts import render

# Create your views here.
from django.views.generic import (
  ListView
 )

from .models import Persona
#listar todos los empleados de la empresa
class listAllEmpleados(ListView):
  template_name = 'empleado/lista_all.html'
  paginate_by=4
  model=Persona

class listByAreaEmpleado(ListView):
  """ Lista empleados de una area """
  template_name = 'empleado/lista_by_area.html'
  
  def get_queryset(self):
    area = self.kwargs['shorname']
    lista=Persona.objects.filter(
      departamento__name=area
    )
    return lista
  
class ListEmpleadosByKwords(ListView):
  "lista de empleados por palabra clave"
  template_name = 'empleado/by_kwords.html'
  context_object_name='empleados'

  def get_queryset(self):    
    palabra_clave=self.request.GET.get('kword')
    lista = Persona.objects.filter(
      first_name=palabra_clave
    )
    return lista


class ListaHabilidadesEmpleado(ListView):
  template_name = "empleado/habilidad.html"
  context_object_name='habilidades'

  def get_queryset(self):
    id_empleado=self.kwargs['id']
    empleado=Persona.objects.get(id=id_empleado)
    return  empleado.habilidades.all()
  

