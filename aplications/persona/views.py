from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import (
  ListView,
  DetailView,
  CreateView,
  TemplateView,
  UpdateView,
  DeleteView
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


class EmpleadosDetailView(DetailView):
  model = Persona
  template_name = "empleado/detail_empleado.html"
  
  def get_context_data(self, **kwargs):
    context = super(EmpleadosDetailView, self).get_context_data(**kwargs)
    context['title'] = 'Empleado del mes'
    return context
  


class SuccessView(TemplateView):
  template_name ='empleado/success.html'

class EmpleadopCreateView(CreateView):
  """crea formulario"""
  model = Persona
  template_name = "empleado/add.html"
  fields = [
    'first_name', 
    'last_name', 
    'job', 
    'departamento', 
    'habilidades'
    ]
  #fields = ('__all__') 
  success_url = reverse_lazy('personal_app:correcto')
  def form_valid(self, form):
    #logica del proceso
    empleado=form.save(commit=False)#aqui ya se guardo
    empleado.full_name = empleado.first_name + ' ' + empleado.last_name
    empleado.save()
    return super(EmpleadopCreateView,self).form_valid(form)



class EmpleadoUpdateView(UpdateView):  
  template_name = "empleado/update.html"
  model = Persona
  fields = [
    'first_name',
    'last_name',
    'job',
    'departamento',
    'habilidades'
  ]
  success_url = reverse_lazy('personal_app:correcto')

  def post(self, request, *args, **kwargs):
    self.object=self.get_object()
    print('************** Metodos POST *********************')    
    print(request.POST['last_name'])
    return super().post(request, *args, **kwargs)
  
  def form_valid(self, form):
    print('************** Metodos form  *********************')
    print('***********************************')
    return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
  model = Persona
  template_name = "empleado/delete.html"
  success_url = reverse_lazy('personal_app:correcto')
