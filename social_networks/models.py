from django.db import models

# Create your models here.
from django.db import models

class SocialMediaProfile(models.Model):
    ICON_CHOICES = [
        ('fa-facebook', 'Facebook'),
        ('fa-x-twitter', 'X'), 
        ('fa-instagram', 'Instagram'),
        ('fa-linkedin', 'LinkedIn'),
        ('fa-youtube', 'YouTube'),
        ('fa-github', 'GitHub'),
    ]

    icon = models.CharField(max_length=50, choices=ICON_CHOICES)
    url = models.URLField(max_length=200)

    def __str__(self):
        return f"{self.get_icon_display()} - {self.url}"
