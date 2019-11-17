from django.views.generic import View, TemplateView
from django.http import HttpResponse


class PostListView1(View):
    def get(self, request):
        name = '공유'
        html = self.get_template_string().format(name=name)
      
        return HttpResponse(html)

    def get_template_string(self):
        return '''
               <h1>AskDjango</h1>
                <p>{name}</p>
                <p>여러분의 파이썬 페이커</p>
        '''


post_list1 = PostListView1.as_view()

#정확히 views에 있는 것과 같은 역할을 한다. 클래스의 장점이 위에 보여짐

class PostList2(TemplateView):
    template_name = 'dojo/post_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['name']= '공유'
        return context
 
post_list2 = PostList2.as_view() #클래스를 뷰로 바꿔주는 것@!

class PostList3(object):
    pass

class ExcelDownloadView(View):
    excel_path = '/other/path/excel.xls'
