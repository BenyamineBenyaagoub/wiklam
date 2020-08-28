from .views import * 
from django.urls import include, path
from django.conf.urls import url, include
from django.conf.urls import handler404
from django.contrib.auth import views as auth_views



#handler404 = notfound

urlpatterns = [
    path('consultorio/', PreguntaView.list_preguntas , name='blog'),
    path('consultorio/<pregunta>', PreguntaView.show , name='blog'),
    path('consultorio/category/<category>/', PreguntaView.list_pregunta_cetegory , name='show_post'),
    path('consultorio/nueva_consulta/', PreguntaView.insert , name='blog'),
    path('respuesta/crear/<pregunta>/', RespuestaView.insert , name='blog'),
    path('respuesta/r/crear/<pregunta>/', RespuestaView.insert_r , name='blog'),

]

