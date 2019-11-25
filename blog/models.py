from django.db import models
import re
from django.forms import ValidationError
from django.conf import settings
from django.urls import reverse
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail


def lnglat_validator(value):
     if not re.match(r'^([+-]?\d+\.?\d*).([+-]?\d+\.?\d*)$', value):
          raise ValidationError('Invalid LngLat Type')


class Post(models.Model):
    STATUS_CHOICES = (
        ('d', "Draft"),#('저장될 값', 'UI에 보여질 레이블')
        ('p', 'Published'),
        ('w', 'Withdrawn'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=100, verbose_name="제목",
    help_text="포스팅 제목을 입력해주세요") #길이 제한이 있는 문자열
    tags = models.CharField(max_length=100, blank=True)
          #blank 디폴트는 false. 기본은 필수요소임
    Inglat = models.CharField(max_length=50, blank=True,
    validators=[lnglat_validator],
    help_text="경도/위도 포맷으로 입력")
    content = models.TextField(verbose_name="내용") #길이 제한이 없는 문자열 #DB는 문자열길이차이에서 구별필요하므로 속도차이

    photo = ProcessedImageField(blank=True, upload_to='blog/post/%y/%m/%d',
                                processors=[Thumbnail(300, 300)],
                                format='JPEG',
                                options={'quality': 60})


    tag_set = models.ManyToManyField('Tag', blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True) #날짜시간 필드
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
 
    class Meta:
        ordering = ['-id'] #이 필드에 대해서 내림차순 정렬
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[ self.id ]) #reverse는 주소 문자열리턴해줌


    
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  #
    author = models.CharField(max_length=20)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name






# Create your models here.
