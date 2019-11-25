from django import forms
from django.views.generic import ListView, CreateView, DetailView
from .models import Post

post_list = ListView.as_view(model=Post, paginate_by=10)

post_detail = DetailView.as_view(model=Post)
