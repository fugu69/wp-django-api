from django import forms
from .models import ArticleArticle

class ArticleForm(forms.ModelForm):
    class Meta:
        model = ArticleArticle
        fields = ['title']
