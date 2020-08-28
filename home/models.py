from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

# Create your models here.

class User(AbstractUser):
    biografia = models.CharField(blank=True, null = True,max_length=255)
    is_moder = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    nombre = models.CharField(max_length=55)
    apellido = models.CharField(max_length=55)
    sigue = models.ForeignKey('self',null=True, blank=True, related_name="sigue_r" , on_delete=models.CASCADE)
    followers = models.ManyToManyField('self', related_name='followers_related', symmetrical=False)
    following = models.ManyToManyField('self', related_name='follows_related', symmetrical=False)
    logo = models.FileField(upload_to='home/photos', default="perfil.png")
    date_modified = models.DateTimeField(auto_now=True)


