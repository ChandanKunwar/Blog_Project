from django import forms
from django.db.models import fields
from .models import PostModel,comment

class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':4}))
    class Meta:
        model = PostModel
        fields = ('title', 'content')

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title','content')

class CommentForm(forms.ModelForm):
    content = forms.CharField(label = "", widget=forms.TextInput(attrs={'placeholder':"Add comment here..."}))
    class Meta:
        model = comment
        fields = ('content',)
