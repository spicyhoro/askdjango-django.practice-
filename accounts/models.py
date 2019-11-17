from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

#User는 장고 기본이므로 수정못함 야ㅕ기다가 추가정보제공하고싶으니까 onetoone을 만들어!


# Create your models here.
