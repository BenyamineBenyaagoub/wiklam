from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    sigue = models.ForeignKey('self',null=True, blank=True, related_name="sigue_r" , on_delete=models.CASCADE)
    followers = models.ManyToManyField('self', related_name='followers_related', symmetrical=False)
    following = models.ManyToManyField('self', related_name='follows_related', symmetrical=False)
    logo = models.FileField(upload_to='img/users', default="perfil.png")
    date_modified = models.DateTimeField(auto_now=True)


