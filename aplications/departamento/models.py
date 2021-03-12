from django.db import models

# Create your models here.

class Departamento(models.Model):
  name =models.CharField('Nombre',max_length=50)
  shor_name = models.CharField('Nombre_corto', max_length=20,unique=True)
  anulate = models.BooleanField('Anulado',default=False)

  class Meta:
    verbose_name='Mi departamento'
    verbose_name_plural='Areas de la empresa'
    ordering=['name']
    #orden inverso ordering=[-'name']
    #indica que no quiero que se registre algo similar entre estas dos 
    #unique_together=('name','shor_name')
    #ordering = [name] inverso
  def __str__(self):
      return self.name + ' ' + self.shor_name
  
      
