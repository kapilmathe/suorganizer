from django.conf.urls import url
from organizer.views import tag_list,tag_detail,startup_list,startup_detail,tag_create,TagCreate,TagUpdate,TagDelete
urlpatterns = [

    url(r'^$',tag_list,name='organizer_tag_list'),
    url(r'^create/$',TagCreate.as_view(),name='organizer_tag_create'),
    url(r'^(?P<slug>[\w\-]+)/$',tag_detail,name='organizer_tag_detail'),
    url(r'^(?P<slug>[\w\-]+)/update/$',TagUpdate.as_view(),name='organizer_tag_update'),
    url(r'^(?P<slug>[\w\-]+)/delete/$',TagDelete.as_view(),name='organizer_tag_delete'),

    # url(r'^startup/$',startup_list,name='organizer_startup_list'),
    # url(r'^startup/(?P<slug>[\w\-]+)/$',startup_detail,name='organizer_startup_detail')
]