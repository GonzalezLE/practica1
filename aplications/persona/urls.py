from django.contrib import admin
from django.urls import path

def DesadePeople(self):
  print('======DESDE PEOPLE ===========')
    

urlpatterns = [
    path('persona/', DesadePeople),
]
