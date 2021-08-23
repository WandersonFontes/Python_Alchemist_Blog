from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Post, Profile, TagPost


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title', 
            'subtitle', 
            'body', 
            'publish_date',
            'published',
            'author',
            'tags'
        ]
