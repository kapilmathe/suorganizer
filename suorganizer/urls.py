"""suorganizer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

from blog import urls as blog_urls
from organizer.urls import tag_urls,startup_url,newslink_url
from suorganizer.views import redirect_root
from staticpage import urls as static_url
from contact import urls as contact_url
# from staticpage.views import contact,about

urlpatterns = [
    url(r'^$', redirect_root),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tag/',include(tag_urls)),
    url(r'^blog/',include(blog_urls)),
    url(r'^startup/',include(startup_url)),
    url(r'^newslink/',include(newslink_url)),
    url(r'^staticpage/',include(static_url),name='about'),
    url(r'^contact/',include(contact_url)),
]
