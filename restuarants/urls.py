from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^home1/$', views.restaurant_list, name= "home1"),
    url(r'^home2/(?P<restaurant_id>\d+)/$', views.restaurant_detail, name= "home2")

]
