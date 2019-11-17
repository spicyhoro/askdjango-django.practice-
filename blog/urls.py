# blog/urls.py
from django.conf.urls import url
from django.urls import include, path
from . import views



app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>', views.post_detail, name='post_detail'),
    path('new/', views.post_new, name='post_new'),
    path('<int:id>/edit/', views.post_edit, name='post_edit'),
]
#정규표현식 문자열 시작 ^ 끝 $
#함수를 인자로 넘겨줌 (호출x ()없으므로)
#blop/다음에 숫자가 들어오면 <id>는 받을 인자이름 d+는 숫자하나이상있으면 id라는 이름으로 뷰에 패스
