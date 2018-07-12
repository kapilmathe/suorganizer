from django.conf.urls import url
from .views import post_list,post_detail,PostCreate,PostUpdate,PostDelete
urlpatterns = [
    url(r'^$',post_list,name='blog_post_list'),
    url(r'^(?P<year>\d{4})/'
        r'(?P<month>\d{1,2})/'
        r'(?P<slug>[\w\-]+)/$',
        post_detail,
        name='blog_post_detail'),
    url(r'^create/$',PostCreate.as_view(),name='blog_post_create'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/update/$',PostUpdate.as_view(),name='blog_post_update'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>[\w\-]+)/delete/$',PostDelete.as_view(),name='blog_post_delete'),
]