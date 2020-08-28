from django.db import models
from home.models import *
from post.models import Category
# Create your models here.
class Pregunta(models.Model):
    """Pregunta model."""
    title = models.CharField(max_length=255)

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    pregunta = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=True)
    views = models.PositiveIntegerField(default=0)
    reports = models.ManyToManyField(User, related_name='reports_related_p', symmetrical=False)
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ('pregunta',)

    def __str__(self):
        return '{} by @{}'.format(self.pregunta, self.user.username)

class Respuesta(models.Model):
    """Respuesta model."""
    text =  models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    pregunta = models.ForeignKey(Pregunta, on_delete=models.PROTECT)
    likes = models.ManyToManyField(User, related_name='likes_related_r', symmetrical=False)
    dislikes = models.ManyToManyField(User, related_name='dislikes_related_r', symmetrical=False)
    reports = models.ManyToManyField(User, related_name='reports_related_r', symmetrical=False)
    respuesta = models.ManyToManyField("self" , related_name='respuesta_related_r', symmetrical=False)
    created = models.DateTimeField(auto_now_add=True)
    eshijo = models.BooleanField(default=False)