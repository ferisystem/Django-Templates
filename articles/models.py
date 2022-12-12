from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save, post_save
from .utils import slugify_instance_title
from django.urls import reverse


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = models.SlugField(unique=True, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(
        auto_now_add=False,
        auto_now=False,
        null=True,
        blank=True
    ) # you can use "default=timezone.now" too

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"slug": self.slug})

    def get_absolute_url_old(self):
        return f'/articles/{self.slug}/'
    
    def save(self, *args, **kwargs):
        # if self.slug is None:
            # self.slug = slugify(self.title)
        super().save(*args, **kwargs)


def article_pre_save(sender, instance, *args, **kwargs):
    if instance.slug is None:
        slugify_instance_title(instance, save=False)

pre_save.connect(article_pre_save, sender=Article)


def article_post_save(sender, instance, created, *args, **kwargs):
    if created:
       slugify_instance_title(instance, save=True)

post_save.connect(article_post_save, sender=Article)