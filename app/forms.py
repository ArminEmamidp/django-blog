from django import forms

from .models import Comment



class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user_name', 'body']
        widgets = {
            'user_name' : forms.TextInput(attrs={'placeholder':'Enter your name...', 'class':'form-control'}),
            'body' : forms.Textarea(attrs={'placeholder':'Enter your comment...', 'class':'form-control'})
        }