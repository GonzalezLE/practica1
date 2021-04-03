from django.contrib import admin
from django.urls import path

from . import views

app_name='personal_app'

urlpatterns = [
  path(
    '',
    views.InicioView.as_view(),
    name='inicio'
  ),
  path('listar-todo-empleados/', 
    views.listAllEmpleados.as_view(),
       name='empleados_all'
  ),
  path(
      'listar-by-area/<shorname>/',
    views.listByAreaEmpleado.as_view(),
      name='empleados_area'
  ),
  path('buscar-empleado/', views.ListEmpleadosByKwords.as_view()),
  path('lista-habilidades/<id>', views.ListaHabilidadesEmpleado.as_view()),
  path(
    'ver-empleado/<pk>/', 
    views.EmpleadosDetailView.as_view(),
    name='empleado_detail'),
  path('add-empleado/', views.EmpleadopCreateView.as_view()),
  path(
    'success/', 
    views.SuccessView.as_view(), 
    name='correcto'
  ),
  path(
    'update-empleado/<pk>/', 
    views.EmpleadoUpdateView.as_view(),
    name='modificar_empleado'),
  path(
    'delete-empleado/<pk>/',
    views.EmpleadoDeleteView.as_view(),
    name='eliminar_empleado'
  )
]
