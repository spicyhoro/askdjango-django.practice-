from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse ,JsonResponse
import os
from django.conf import settings
from .forms import PostForm
from .models import Post
from django.views.generic import ListView
from .models import Post
from django.views.generic import DetailView, ListView


post_detail = DetailView.as_view(model=Post)

post_list = ListView.as_view(model=Post, paginate_by=3)


def mysum(request, numbers):
    result = sum(map(int, numbers.split("/")))  #map은 리스트의 요소를 지정된 함수로 처리해주는 함수입니

    return HttpResponse(result)

def name(request, name, age):
    result = f"안녕하세요. {name}. {age}살이시네요."

    return HttpResponse(result)
# Create your tests here.

# Create your views here.


def excel_download(request):
    filepath = "/Users/spicyhoro/nomade/django/cat.xls"
    settings.BASE_DIR
    filename = os.path.basename(filepath)
    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        #위에는 필요한 응답헤더 세팅
        return response

def post_new(request):
   if request.method == "POST":
       form = PostForm(request.POST, request.FILES)
       if form.is_valid():
           post = form.save()
           post.ip = request.META['REMOTE_ADDR']
           post.save()
           return redirect('/dojo/')

   else:   #이게 GET요청일때 실행되는것임
       form = PostForm()
       pass
   return render(request, 'dojo/post_form.html', {
       'form': form,
   })


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect('/dojo/')

    else:  # 이게 GET요청일때 실행되는것임
        form = PostForm(instance=post)
        pass
    return render(request, 'dojo/post_form.html', {
        'form': form,
    })

