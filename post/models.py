from django.db import models
from home.models import *
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


class Category(models.Model):
    """Category model."""
    name =  models.CharField(max_length=255)
# Create your models here.
    def __str__(self):
            """Return title and username."""
            return self.name

class Post(models.Model):
    """Post model."""
    
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    image_header = models.ImageField(upload_to='posts/photos')
    post = RichTextField(blank=True, null = True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=True)
    url = models.SlugField(max_length=255, unique=True)
    views = models.PositiveIntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='likes_related', symmetrical=False)
    dislikes = models.ManyToManyField(User, related_name='dislikes_related', symmetrical=False)
    reports = models.ManyToManyField(User, related_name='reports_related', symmetrical=False)
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ('title',)


    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.title, self.user.username)


    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Post, self).save(*args, **kwargs)



class Comment(models.Model):
    """Category model."""
    text =  models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    likes = models.ManyToManyField(User, related_name='likes_related_c', symmetrical=False)
    dislikes = models.ManyToManyField(User, related_name='dislikes_related_c', symmetrical=False)
    reports = models.ManyToManyField(User, related_name='reports_related_c', symmetrical=False)
    created = models.DateTimeField(auto_now_add=True)
   
