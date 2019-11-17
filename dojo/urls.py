from django.conf.urls import url
from django.urls import path
from . import views
from . import views_cbv

app_name = 'dojo'
urlpatterns = [
    url(r'^new/$', views.post_new),
    url(r'^(?P<id>\d+)/edit/$', views.post_edit),

    url(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    url(r'^hello/(?P<name>[ㄱ-힣]{1,3})/(?P<age>[0-9]{1,2})/$', views.name),
    path('list2', views.post_list2),
    path('list3', views.post_list3),
    path('excel/', views.excel_download),

    path('cbv/list2/', views_cbv.post_list2),
    path('<int:id>', views.post_detail),
    #url(r'^cbv/list3/$', views_cbv.post_list3),
    #url(r'^cbv/excel/$', views_cbv.excel_download),
]