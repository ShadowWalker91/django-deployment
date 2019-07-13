from django.conf.urls import  url
from Course_Application_1 import views


urlpatterns= [
    url('', views.index, name="index"),
]