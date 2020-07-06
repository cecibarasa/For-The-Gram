from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path


urlpatterns=[
    url('^$', views.home, name='instaToday'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^likes/(\d+)', views.likes, name="likes"),
    url(r'^posts/', views.profile, name='profile'),
    url(r'^follow(\d+)', views.follow, name="follow"),
    url(r'^comment/(\d+)', views.comment, name="comment"),
    url(r'^commenting/(\d+)', views.commenting, name="commenting"),
    url(r'^search/$', views.search_user, name="search"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)