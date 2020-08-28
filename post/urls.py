
from .views import * 
from django.urls import include, path
from django.conf.urls import url, include
from django.conf.urls import handler404
from django.contrib.auth import views as auth_views



#handler404 = notfound

urlpatterns = [
    path('blog/crear/', PostView.insert , name='crear_post'),
    path('blog/', PostView.list_post , name='blog'),
    path('post/like', PostView.like , name='like_post'),
    path('post/dislike', PostView.dislike , name='dislike_post'),

    path('blog/<post>/', PostView.show , name='show_post'),
    path('blog/category/<category>/', PostView.list_post_cetegory , name='show_post'),
    path('comment/crear/<post>/', CommentView.insert  , name='show_post'),


]





