from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone

class Article(models.Model):
    title = models.CharField(max_length=200, blank=False, unique=True)
    description = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    content = HTMLField()  # Usamos HTMLField de tinymce en lugar de CharField o TextField
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title
