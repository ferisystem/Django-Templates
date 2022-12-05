from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(
        auto_now_add=False,
        auto_now=False,
        null=True,
        blank=True
    ) # you can use "default=timezone.now" too