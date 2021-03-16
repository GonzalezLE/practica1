from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
  path('listar-todo-empleados/', views.listAllEmpleados.as_view()),
  path('listar-by-area/<shorname>/', views.listByAreaEmpleado.as_view()),
  path('buscar-empleado/', views.ListEmpleadosByKwords.as_view()),
  path('lista-habilidades/<id>', views.ListaHabilidadesEmpleado.as_view()),
]
