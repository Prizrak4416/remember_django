from django import forms
from .models import Category, News
import re
from django.core.exceptions import ValidationError


# формы не связаные с моделями
# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Название ', widget=forms.TextInput(attrs={'class': 'form-control'}))
#     content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}), label='Текст ', required=False)
#     is_published = forms.BooleanField(label='Опубликованно ', initial=True)
#     category = forms.ModelChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), empty_label='Выберите категорию', queryset=Category.objects.all(), label='Категория ')

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цивры.')
        return title
