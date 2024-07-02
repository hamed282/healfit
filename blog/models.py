from django.db import models
from tinymce.models import HTMLField


class BlogModel(models.Model):
    cover_image = models.ImageField(upload_to='blog/cover/')
    banner = models.ImageField(upload_to='blog/banner/')
    title = models.CharField(max_length=250)
    title_image = models.ImageField(upload_to='blog/title/')
    description = models.TextField()
    body = HTMLField()
    author = models.CharField(max_length=64)
    role = models.CharField(max_length=24)
    slug = models.SlugField()
    category = models.CharField(max_length=24)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
