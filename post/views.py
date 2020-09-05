from django.shortcuts import render , redirect
from django.views.generic import CreateView, TemplateView , ListView
from .forms import *
from .models import *
from pregunta.models import *
from django.contrib.auth import login, authenticate
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required

# Create your views here.
class PostView(TemplateView):
           
    @login_required     
    def insert(request):

        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            print("s")
            if form.is_valid():
                print("a")
                if request.FILES:
                    myfile = request.FILES['image_header']
                    fs = FileSystemStorage()
                    filename = fs.save( myfile.name, myfile)
                    uploaded_file_url = fs.url(filename)     
                post = form.save()
                post.refresh_from_db()  
                post.save()
                return redirect(f"/blog/{post.url}")
        else:
            form = PostForm()
        return render(request, 'post/crear.html', {'form': form})

    def editar(request,post):

        i = Post.objects.get(url = post)

        if( i.user == request.user ):

            form = PostForm(request.POST or None, request.FILES or None, instance = i )

            if request.method == 'POST':
                print("s")
                if form.is_valid():
                    print("a")
                    if request.FILES:
                        myfile = request.FILES['image_header']
                        fs = FileSystemStorage()
                        filename = fs.save( myfile.name, myfile)
                        uploaded_file_url = fs.url(filename)     
                    post = form.save()
                    post.refresh_from_db()  
                    post.save()
                    return redirect(f"/blog/{post.url}")
        
                
            return render(request, 'post/editar.html', {'form': form})

        else:

            return redirect("/")

    def show(request, post):

        like = False

        dislike = False

        category = Category.objects.all()

        posts = Post.objects.all().order_by('-id')[:5:1]
        
        post = Post.objects.get(url = post)

        posta = Post.objects.filter(pk = post.id).update(views = (post.views+1)) 

        coments = Comment.objects.filter(post = post)  
        
        if request.user in post.likes.all():
            like = True
            
        if request.user in post.dislikes.all():
            dislike = True

        return render(request,"post/show.html",{"post":post ,"posts":posts ,"categorys":category , 'comments':coments , 'like':like , 'dislike':dislike})


    def list_post(request):
        category = Category.objects.all()

        pposts = Post.objects.all().order_by('-views')[:5:1]

        preguntas = Pregunta.objects.all().order_by('-id')[:5:1]


        post = Post.objects.all().order_by('-id')

        return render(request,"post/list.html",{"posts":post,"pposts":pposts,"categorys":category, 'preguntas': preguntas})

    @login_required     
    def like(request):

        if request.method == 'POST':

            user = User.objects.get(pk = request.POST.get("user"))

            post = Post.objects.get(pk = request.POST.get("post")) 
            
            post.dislikes.remove(user)

            post.likes.add(user)


        return redirect(f"/blog/{post.url}")

    @login_required     
    def dislike(request):

        if request.method == 'POST':

            user = User.objects.get(pk = request.POST.get("user"))

            post = Post.objects.get(pk = request.POST.get("post")) 
            
            post.likes.remove(user)
            post.dislikes.add(user)

        return redirect(f"/blog/{post.url}")


    def list_post_cetegory(request,category):  

        pposts = Post.objects.all().order_by('-views')[:5:1]

        preguntas = Pregunta.objects.all().order_by('-id')[:5:1]

        category = Category.objects.get(name=category)
        
        post = Post.objects.filter(categories = category.id).order_by('-id')

        category = Category.objects.all()

        return render(request,"post/list.html",{"posts":post,"pposts":pposts,"categorys":category, 'preguntas': preguntas})

class CommentView(TemplateView):

    @login_required     
    def insert(request , post):
        instance = Post.objects.get(pk = post)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():             
                comment = form.save()
                comment.refresh_from_db()  
                comment.save()

        return redirect(f"/blog/{instance.url}")


  