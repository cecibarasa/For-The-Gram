from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path


urlpatterns=[
    url('^$', views.home, name='instaToday'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^likes/<image_id>', views.likes, name="likes"),
    url(r'^posts/', views.profile, name='profile'),
    # re_path(r'^follow/(?P<operation>.+)/(?P<pk>\d+)/$', views.follow, name="follow"),
    url(r'^comment/(\d+)', views.comment, name="comment"),
    url(r'^commenting/(\d+)', views.commenting, name="commenting"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)