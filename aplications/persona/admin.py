from django.contrib import admin

# Register your models here.
from .models import Persona,Habilidades


admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
  list_display=(
      'first_name',
      'last_name',
      'departamento',
      'job',
      'full_name'
  )
  #
  def full_name(self,obj):    
    return obj.first_name + ' ' + obj.last_name
  #
  search_fields=(
    'first_name', 
  )
  list_filter = ('job', 'departamento')
  #solo funciona para las many to many
  filter_horizontal = ('habilidades',)


admin.site.register(Persona,EmpleadoAdmin)
