
from .views import * 
from django.urls import include, path
from django.conf.urls import url, include
from django.conf.urls import handler404
from django.contrib.auth import views as auth_views



#handler404 = notfound

urlpatterns = [
    path('', cargar_home),
    path('registro/', Signup.signup , name='registros'),
    path('login/',  auth_views.LoginView.as_view(template_name="login.html") , name='login'),
    path('djrichtextfield/', include('djrichtextfield.urls'))

]





