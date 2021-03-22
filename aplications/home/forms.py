from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):
  class Meta:
    model = Prueba
    #fields=('__all__')
    fields = (
      'titulo', 
      'subtitulo', 
      'cantidad'
    )
    widgets={
      'titulo':forms.TextInput(
        attrs={
          'placeholder':'Escribir',
          'class':'form-control'
        }
      )
    }

  def clean_cantidad(self):
    cantidad = self.cleaned_data["cantidad"]
    if cantidad < 10:
      return forms.ValidationError('Ingrese aun numero mayor a 10')

    return cantidad
  
