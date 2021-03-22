from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import(
  FormView
)

#importamos los modelos
from aplications.persona.models import Persona
from .models import Departamento

from .forms import NewDepartamentoForm


class NewDepartamentoView(FormView):
  template_name='departamento/new_departamento.html'
  form_class=NewDepartamentoForm
  success_url='/'

  def form_valid(self, form):
    depa=Departamento(
      name=form.cleaned_data['departamento'],
      shor_name=form.cleaned_data['shorname']
    )
    depa.save()
    print('***************************')
    name=form.cleaned_data['nombre']
    apellidos = form.cleaned_data['apellidos']
    
    Persona.objects.create(
      first_name=name,
      last_name=apellidos,
      job=1,
      departamento=depa
    )
    return super(NewDepartamentoView, self).form_valid(form)

