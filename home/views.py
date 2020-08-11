from django.shortcuts import render 
from django.views.generic import CreateView, TemplateView , ListView
from .forms import *
from django.contrib.auth import login, authenticate

# Create your views here.


def cargar_home(request):
    return render(request,"index.html")

class LoginView(TemplateView):

    template_name = 'login.html'
    
def notfound(request, exception):
    return render(request,'400.html')



class Signup(TemplateView):
     
    def signup(request):

        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                user.refresh_from_db()  
                user.save()
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=user.username, password=raw_password)
                login(request, user)
                return render(request, 'alert.html',{'alert' : "Se ha creado el usuario con éxito!" , 'class' : "success"}  ) 
        else:
            form = SignUpForm()
        return render(request, 'signup.html', {'form': form})
