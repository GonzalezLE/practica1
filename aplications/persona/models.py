from django.db import models
from aplications.departamento.models import Departamento
# Create your models here.
class Persona(models.Model):
  """ Modelo para la tabla empleado """
  # Contador
  # Administrador
  # Economista
  # Otro
  JOB_CHOICES=(
      ('0', 'Contador'),
      ('1', 'Administrador'),
      ('2', 'Economista'),
      ('3', 'Otro')
  )
  first_name = models.CharField('Nombres', max_length=50)
  last_name = models.CharField('apellidos', max_length=50)
  job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
  departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
  #image = models.ImageField(, upload_to=None, height_field=None, width_field=None, max_length=None)
  class Meta:
    verbose_name='Persona'
    verbose_name_plural='Personas de la empresa'
    ordering = ['last_name']


  def __str__(self):
    return self.first_name
