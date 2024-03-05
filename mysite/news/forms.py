from django import forms
from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Название ', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}), label='Текст ', required=False)
    is_published = forms.BooleanField(label='Опубликованно ', initial=True)
    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), empty_label='Выберите категорию', queryset=Category.objects.all(), label='Категория ')
