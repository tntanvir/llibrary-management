from django import forms
from .models import book,BookComment


class BookForm(forms.ModelForm):
    class Meta:
        model = book
        exclude = ['author']

class CommentForm(forms.ModelForm):
    class Meta:
        model=BookComment
        fields=['name', 'comment']