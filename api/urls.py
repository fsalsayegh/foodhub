from django.conf.urls import url
from . import views

urlpatterns = [
    #path list/create/detail/delete or update 
    url(r'^$', views.RestaurantListAPIView.as_view(), name='restaurant_list'), 
    url(r'^create/$', views.RestaurantCreateAPIView.as_view(), name='restaurant_create'),
    url(r'^(?P<slug>[-\w]+)/$', views.RestaurantDetailAPIView.as_view(), name='restaurant_detail'), 
    url(r'^(?P<slug>[-\w]+)/update/$', views.RestaurantUpdateAPIView.as_view(), name='restaurant_update'),
    url(r'^(?P<slug>[-\w]+)/delete/$', views.RestaurantDeleteAPIView.as_view(), name='restaurant_delete'),

    ]