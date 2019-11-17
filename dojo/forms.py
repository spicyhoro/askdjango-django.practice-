from django import forms
from .models import Post, GameUser

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        #fields = '__all__' 이것도 가능
        fields = ['title', 'content', 'user_agent']
        widgets  = {
            'user_agent': forms.HiddenInput,
        }


'''
    def save(self, commit=True):
        post = Post(**self.cleaned_data)

        if commit:
             post.save()
        return post
'''

