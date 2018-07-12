from __future__ import unicode_literals
from django.db import models
from organizer.models import Startup,NewsLink,Tag, TagSerializer, TagModelSerializer
from django.core.urlresolvers import reverse
from rest_framework import  serializers

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=512)
    slug = models.SlugField(max_length=63,unique_for_month='pub_date')
    text = models.TextField()
    pub_date = models.DateField('date published',auto_now_add=True)
    tag = models.ManyToManyField(Tag,blank=True,related_name='blog_posts')
    startups = models.ManyToManyField(Startup,blank=True,related_name='blog_post')

    def __str__(self):
        return "{} on {}".format(self.title,self.pub_date.strftime('%Y-%m-%d'))

    def get_absolute_url(self):
        return reverse('blog_post_detail',kwargs={
            'year':self.pub_date.year,
            'month':self.pub_date.month,
            'slug':self.slug
        })

    def get_update_url(self):
        return reverse('blog_post_update',
                       kwargs={'year':self.pub_date.year,
                               'month':self.pub_date.month,
                               'slug':self.slug})

    def get_delete_url(self):
        return reverse('blog_post_delete',
                       kwargs={'year':self.pub_date.year,
                               'month':self.pub_date.month,
                               'slug':self.slug})

class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=512)
    slug = serializers.SlugField(max_length=63)
    text = serializers.CharField(max_length=2048)
    tag = TagSerializer(required=False, many=True)

class PostModelSerializer(serializers.ModelSerializer):
    tag = TagModelSerializer(read_only=True, many=True)
    class Meta:
        model = Post
        fields = '__all__'
        depth = 1