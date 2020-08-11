from django.shortcuts import render , redirect
from django.views.generic import CreateView, TemplateView , ListView
from .forms import *
from .models import *
from django.contrib.auth import login, authenticate
from django.core.files.storage import FileSystemStorage

# Create your views here.
class PostView(TemplateView):
           
         
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
                return PostView.show(request, post.id)
        else:
            form = PostForm()
        return render(request, 'post/crear.html', {'form': form})


    def show(request, post):
        
        post = Post.objects.get(pk = post) 

        coments = Comment.objects.filter(post = post)  
        
        return render(request,"post/show.html",{"post":post , 'comments':coments})


    def list_post(request):
        
        post = Post.objects.all()

        return render(request,"post/list.html",{"posts":post})


class CommentView(TemplateView):
     
    def insert(request , post):

        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():             
                comment = form.save()
                comment.refresh_from_db()  
                comment.save()

        return redirect(f"/blog/{post}")