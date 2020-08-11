
from django.forms import ModelForm

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()
#aqui se hace un import de los modelos que se necesitan
from .models import *

class SignUpForm(UserCreationForm):


    class Meta:
        model = User
        fields = ['username' , 'password1', 'password2' , 'email' ] 
       
    """     def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['agente'].required = False
        self.fields['empleado'].required = False
        self.fields['logo'].required = False """