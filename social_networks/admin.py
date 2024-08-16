from django.contrib import admin
from .models import SocialMediaProfile

# Register your models here.
@admin.register(SocialMediaProfile)
class SocialMediaProfileAdmin(admin.ModelAdmin):
    list_display = ('icon', 'url')