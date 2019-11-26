from django.conf.urls import url
from accounts import views
from django.urls import path

urlpatterns = [
    path('profile/', views.profile),
    path('signup/', views.signup, name='signup'),
]