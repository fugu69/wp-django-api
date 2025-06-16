from django import forms
from .models import ArticleArticle, PlayerPlayer

class ArticleForm(forms.ModelForm):
    class Meta:
        model = ArticleArticle
        fields = ['title', 'body', 'pinned']

class PlayerPlayerUpdateForm(forms.ModelForm):
    class Meta:
        model = PlayerPlayer
        fields = ['nickname', 'level', 'exp']