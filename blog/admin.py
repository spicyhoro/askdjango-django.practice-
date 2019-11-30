from django.contrib import admin
from .models import Post, Comment, Tag
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'tag_list', 'status', 'content_size','created_at', 'updated_at']
    actions = ['make_draft','make_published']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.prefetch_related('tag_set')

    def tag_list(self, post):
        return ','.join(tag.name for tag in post.tag_set.all()) #리스트로 가져오는 문법
 
    def content_size(self, post):
        return mark_safe('<strong>{}글자</strong>'.format(len(post.content))) #post가 인스턴스 Post의... 

    def make_draft(self, request, queryset):
        updated_count =  queryset.update(status="d") #QuerySet.update
        self.message_user(request, '{}건의 포스팅을 draft상태로 변경'.format(updated_count)) #django message framework 활용
    make_draft.short_description = '지정 포스팅을 draft상태로 변경합니다'

    def make_published(self, request, queryset):
        updated_count =  queryset.update(status="p") #QuerySet.update
        self.message_user(request, '{}건의 포스팅을 Published상태로 변경'.format(updated_count)) #django message framework 활용
    make_published.short_description = '지정 포스팅을 Published상태로 변경합니다'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
     list_display = ['id', 'author', 'post_content_len']


     def post_content_len(self, comment):
         return '{}글자'.format(len(comment.post.content))

     def get_queryset(self, request):
         qs = super().get_queryset(request)
         return qs.select_related('post')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    
    pass