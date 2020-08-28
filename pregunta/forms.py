
from django.forms import ModelForm

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()
#aqui se hace un import de los modelos que se necesitan
from .models import *

class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        fields = ['user', 'title','pregunta','categories']

    def __init__(self, *args, **kwargs):
        super(PreguntaForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = ['user','text','pregunta','eshijo']

    def __init__(self, *args, **kwargs):
        super(RespuestaForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control' 

class ResRespuestaForm(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = ['user','text','pregunta','respuesta']

    def __init__(self, *args, **kwargs):
        super(RespuestaForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control' 