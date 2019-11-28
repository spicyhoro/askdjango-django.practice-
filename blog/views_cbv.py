from django import forms
from django.views.generic import ListView, CreateView, DetailView,UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy


post_list = ListView.as_view(model=Post,
                             queryset=Post.objects.all().prefetch_related('tag_set', 'comment_set'),
                             paginate_by=10)

post_detail = DetailView.as_view(model=Post)


post_new = CreateView.as_view(model=Post, fields='__all__')

post_edit = UpdateView.as_view(model=Post, fields='__all__')

post_delete = DeleteView.as_view(model=Post, success_url=reverse_lazy('blog:post_list'))
