from django.shortcuts import render , redirect
from django.views.generic import CreateView, TemplateView , ListView
from .forms import *
from django.core.files.storage import FileSystemStorage

from post.models import *
from pregunta.models import *

from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, authenticate
from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.


def cargar_home(request):

    from django.db.models import Count

    users = User.objects.annotate(Count('id'))

    comments = Comment.objects.values("id").annotate(Count('id'))

    respuestas = Respuesta.objects.values("id").annotate(Count('id'))

    a = comments.count()

    b = respuestas.count() 

    comments = a + b

    c_posts = Post.objects.values("id").annotate(Count('id'))

    c_preguntas = Pregunta.objects.values("id").annotate(Count('id'))

    posts = Post.objects.all().order_by('-id')[:5:1]

    preguntas = Pregunta.objects.all().order_by('-id')[:7:1]

    return render(request,"index.html", {"users" : users, 'c_preguntas': c_preguntas , 'c_posts' : c_posts,  "comments":comments , 'respuestas' : respuestas , 'posts' : posts , 'preguntas' : preguntas} )


def cargar_politica_de_privacidad(request):
    return render(request,"politica-de-privacidad.html")

class EventosView(TemplateView):
    template_name = 'eventos.html'

class LoginView(TemplateView):
    template_name = 'login.html'


class PerfilView(TemplateView):

    @login_required     
    def get_perfil(request, username):
        user = get_object_or_404(User, username=username)
        preguntas  = Pregunta.objects.filter(user = user.id)
        posts  = Post.objects.filter(user = user.id)
        a = request.user.following.all()

        if(user in a):
            folowing = True
        else:
            folowing = False

        return render(request, 'perfil.html', {'usuario': user , 'folowing': folowing , 'preguntas' : preguntas , 'posts' : posts})
    

def notfound(request, exception):
    return render(request,'400.html')


class Signup(TemplateView):
     
    def signup(request):
        if request.method == 'POST':
            form = SignUpForm(request.POST, request.FILES)
            if form.is_valid():
                if request.FILES:
                    myfile = request.FILES['logo']
                    fs = FileSystemStorage()
                    filename = fs.save( myfile.name, myfile)
                    uploaded_file_url = fs.url(filename)     
                user = form.save()
                user.refresh_from_db()  
                user.save()
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=user.username, password=raw_password)
                login(request, user)
                return redirect("/")
        else:
            form = SignUpForm()
        return render(request, 'signup.html', {'form': form})
        
    @login_required     
    def mod_user(request):
        
        form = ModUserForm(request.POST or None, instance =  request.user)  
        if request.method == 'POST':
            
            if form.is_valid():
                if request.FILES:
                    myfile = request.FILES['logo']
                    fs = FileSystemStorage()
                    filename = fs.save( myfile.name, myfile)
                    uploaded_file_url = fs.url(filename)   
                user = form.save()
                user.refresh_from_db()  
                user.save()
                return redirect(f"/usuario/{user.username}")

                
        else:
            args = {'form': form }
            return render(request, 'modform.html', args)
       
    @login_required     
    def follow(request):

        if request.method == 'POST':

            user = User.objects.get(pk = request.POST.get("user"))

            user.followers.add(request.user)
            request.user.following.add(user)

        return redirect(f"/usuario/{user.username}")

    @login_required     
    def unfollow(request):

        if request.method == 'POST':

            user = User.objects.get(pk = request.POST.get("user"))

            user.followers.remove(request.user)
            request.user.following.remove(user)


        return redirect(f"/usuario/{user.username}")