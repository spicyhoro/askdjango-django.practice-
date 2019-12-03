from django.http import Http404, HttpResponseNotFound
from django.shortcuts import get_object_or_404, render, redirect
from .models import Post, Comment
from .forms import PostForm
from django.contrib import messages

# Create your views here.
def post_list(request):

    qs = Post.objects.all().prefetch_related('comment_set', 'tag_set')

    q = request.GET.get('q', '') #검색이라는 요청에 템플릿에서 나오는 q인자  있다면 q가져오고 없다면 ''으로가져와 객체 q로함리퀘스트 겟인자에 겟에 q가 있
    if q: #q가 True이면 
        qs = qs.filter(title__icontains=q)



    return render(request, 'blog/post_list.html', {'post_list':qs, 'q':q}) 
    #render에 3번쨰 인자로 딕셔너리 형태로 다양한 인자들을 넘겨줄수있다
    # 템플릿에서 q라는 이름의 인자를 넘겨주는걸만들었으므로 


def post_detail(request, id):
    #try:
     #   post = Post.objects.get(id=id)
    #except Post.DoesNotExist:
    #    raise Http404
        
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html',{
        'post':post,
    })


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, '새 포스팅을 저장했습니다.')
            return redirect(post) #post.get_absolute_url()구형되어있음

        pass
    else:
        form = PostForm()

        pass
    return render(request, 'blog/post_form.html',{
        'form':form,
    })


def post_edit(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, '포스팅 수정하였습니다')
            return redirect(post) #post.get_absolute_url()구형되어있음

        pass
    else:
        form = PostForm(instance=post)

        pass
    return render(request, 'blog/post_form.html',{
        'form':form,
    })


def comment_list(request):
    comment_list = Comment.objects.all().select_related('post')
    return render(request, 'blog/comment_list.html', {
        'comment_list': comment_list
    })




def trigger_error(request):
    division_by_zero = 1 / 0
