from django.contrib import admin
from django.urls import path,re_path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    #incluimos la url de las app departamento
    re_path('', include('aplications.departamento.urls')),
    re_path('', include('aplications.persona.urls')),
    re_path('', include('aplications.home.urls'))
]
