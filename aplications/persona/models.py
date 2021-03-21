from django.db import models
from aplications.departamento.models import Departamento
# Create your models here.
from ckeditor.fields import RichTextField

class Habilidades(models.Model):
  habilidad = models.CharField('Habilidad', max_length=50)  
  class Meta:
    verbose_name = 'Habilidad'
    verbose_name_plural = 'Habilidades empleado'
  
  def __str__(self):
    return self.habilidad


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
  full_name = models.CharField(
    'nombre completo', 
    max_length=50,
    blank=True
  )
  job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
  departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
  avatar = models.ImageField(upload_to='empleado', blank=True,null=True)
  habilidades = models.ManyToManyField(Habilidades)
  #cv = RichTextField()
  

  class Meta:
    verbose_name='Persona'
    verbose_name_plural='Personas de la empresa'
    ordering = ['last_name']


  def __str__(self):
    return self.first_name
