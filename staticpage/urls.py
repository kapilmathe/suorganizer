from django.conf.urls import url
from .views import about,contact

urlpatterns = [
    url(r'^about/$',about, name='about'),
    url(r'^contact/$',contact,name='contact_old'),
]