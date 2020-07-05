from django.conf.urls import url
from . import views
from django.conf import settings


urlpatterns=[
    url('^$', views.home, name='instaToday'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^profile$', views.profile, name='profile'),
]