from django import forms
from django.forms import ModelForm

from articles.models import Article


class ArticleForm(ModelForm):

    class Meta:
        model = Article
        fields = ("title", "description", "date")
        widgets = {
            "date": forms.DateInput(attrs={"type": "date",})}
