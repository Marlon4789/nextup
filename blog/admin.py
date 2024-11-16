from django.contrib import admin
from .models import Article
from tinymce.widgets import TinyMCE
from django import forms

class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}, mce_attrs={'height': 700}))

    class Meta:
        model = Article
        fields = '__all__'

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm

admin.site.register(Article, ArticleAdmin)
