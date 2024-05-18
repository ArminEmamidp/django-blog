from django import forms


class CommentForm(forms.Form):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder':'Enter text...', 'class':'form-control', 'label':''}))

class CommentReplyForm(forms.Form):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder':'Enter text...', 'class':'form-control', 'label':''}))


class PostSearchForm(forms.Form):
	search_text = forms.CharField(label='', max_length=200, widget=forms.TextInput(attrs={'placeholder':'Search in posts', 'class':'form-control'}))