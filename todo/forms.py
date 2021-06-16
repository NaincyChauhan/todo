from django import forms
from .models import Post

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title']
        # labels = {'title':'Your Title'}
        widgets = {'title': forms.TextInput(attrs={'class':'form-control col-sm-10', 'placeholder':'write your title here', 'date': forms.DateInput(attrs={'class': 'form-control'})})}