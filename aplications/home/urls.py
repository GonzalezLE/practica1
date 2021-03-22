from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('prueba/',views.PruebaView.as_view()),
    path('lista/',views.PurebaListView.as_view()),
    path('lista-prueba/', views.ListaPrtueba.as_view()),
    path('add/', views.pruebaCreateView.as_view(),name='prueba_add')
]
