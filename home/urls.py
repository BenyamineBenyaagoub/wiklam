
from .views import * 
from django.urls import include, path
from django.conf.urls import url, include
from django.conf.urls import handler404
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.contrib.auth.views import LogoutView


#handler404 = notfound

urlpatterns = [
    url(r'^eventos/$', EventosView.as_view()),
    
    path('', cargar_home , name='home'),
    path('politica_de_cookies/', cargar_politica_de_cookies),
    path('politica_de_privacidad/', cargar_politica_de_privacidad),

    path('u/follow', Signup.follow , name='sign_in'),
    path('u/unfollow', Signup.unfollow , name='sign_in'),

    path('sign_in/', Signup.signup , name='sign_in'),
    path('mod_user/', Signup.mod_user , name='sign_in'),      
    path('login/',  auth_views.LoginView.as_view(template_name="login.html") , name='login'),
    url(r'^logout/$', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),

    path('usuario/<username>/', PerfilView.get_perfil , name='perfil'),
    path('djrichtextfield/', include('djrichtextfield.urls'))

]





