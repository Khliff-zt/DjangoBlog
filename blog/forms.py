from django import forms
from .models import Post

# form logics
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]