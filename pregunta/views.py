from django.shortcuts import render , redirect
from django.views.generic import CreateView, TemplateView , ListView
from .forms import *
from .models import *
from post.models import *
from django.contrib.auth import login, authenticate
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
# Create your views here.

class PreguntaView(TemplateView):
           
    @login_required     
    def insert(request):

        if request.method == 'POST':
            form = PreguntaForm(request.POST)
            if form.is_valid():
                  
                pregunta = form.save()
                pregunta.refresh_from_db()  
                pregunta.save()
                return redirect(f"/consultorio/{pregunta.id}")
        else:
            form = PreguntaForm()
        return render(request, 'pregunta/crear.html', {'form': form})

    def list_preguntas(request):
        category = Category.objects.all()

        posts = Post.objects.all().order_by('-views')[:5:1]
        ppreguntas = Pregunta.objects.all().order_by('-views')[:5:1]
        preguntas = Pregunta.objects.all().order_by('-id')

        return render(request,"pregunta/list.html",{"preguntas":preguntas,"ppreguntas":ppreguntas,"posts":posts , "categorys":category,})


    def list_pregunta_cetegory(request,category):

        category = Category.objects.get(name=category)
        
        preguntas = Pregunta.objects.filter(categories = category.id).order_by('-id')

        category = Category.objects.all()

        posts = Post.objects.all().order_by('-views')[:5:1]
        ppreguntas = Pregunta.objects.all().order_by('-views')[:5:1]

        return render(request,"pregunta/list.html",{"preguntas":preguntas,"ppreguntas":ppreguntas,"posts":posts , "categorys":category,})


    def show(request, pregunta):

        category = Category.objects.all()

        preguntas = Pregunta.objects.all().order_by('-id')[:5:1]
        
        pregunta = Pregunta.objects.get(pk = pregunta)

        p = Pregunta.objects.filter(pk = pregunta.id).update(views = (pregunta.views+1)) 

        respuestas = Respuesta.objects.filter(pregunta = pregunta, eshijo = False)  
        
        posts = Post.objects.all().order_by('-views')[:5:1]


        return render(request,"pregunta/show.html",{"pregunta":pregunta ,"preguntas":preguntas ,"categorys":category ,"posts":posts , 'respuestas':respuestas })

class RespuestaView(TemplateView):

    @login_required     
    def insert(request , pregunta):

        if request.method == 'POST':
            form = RespuestaForm(request.POST)
            if form.is_valid():             
                respuesta = form.save()
                respuesta.refresh_from_db()  
                respuesta.save()

        return redirect(f"/consultorio/{pregunta}")


    @login_required     
    def insert_r(request , pregunta):

        if request.method == 'POST':
            #pregunta_o =  Respuesta.objects.get(pk = request.POST.get("respuesta"))
            form = RespuestaForm(request.POST)
            if form.is_valid():             
                respuesta = form.save()
                respuesta.refresh_from_db()  
                respuesta.save()

        pregunta1 = Respuesta.objects.get(pk = request.POST.get("respuesta"))

        pregunta1.respuesta.add(respuesta)

        return redirect(f"/consultorio/{pregunta}")

        