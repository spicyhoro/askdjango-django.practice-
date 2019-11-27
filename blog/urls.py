# blog/urls.py
from django.conf.urls import url
from django.urls import include, path
from . import views, views_cbv



app_name = 'blog'
urlpatterns = [
    path('', views_cbv.post_list, name='post_list'),
    path('<int:pk>', views_cbv.post_detail, name='post_detail'),
    path('new/', views_cbv.post_new, name='post_new'),
    path('<int:pk>/edit/', views_cbv.post_edit, name='post_edit'),
path('<int:pk>/delete/', views_cbv.post_delete, name='post_delete'),
    path('comments/', views.comment_list, name='comment_list'),
]
#정규표현식 문자열 시작 ^ 끝 $
#함수를 인자로 넘겨줌 (호출x ()없으므로)
#blop/다음에 숫자가 들어오면 <id>는 받을 인자이름 d+는 숫자하나이상있으면 id라는 이름으로 뷰에 패스
