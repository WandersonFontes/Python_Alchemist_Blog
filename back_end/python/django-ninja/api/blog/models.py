from django.db import models
from django.conf import settings


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=240, blank=True)
    class Meta:
        ordering = ('user',)
    def __str__(self):
        return self.user.get_username()

class TagPost(models.Model):
    name = models.CharField(max_length=50, unique=True)
    status = models.BooleanField(default=False)
    class Meta:
        ordering = ('status',)
    def __str__(self):
        return self.name

class Post(models.Model):
    slug = models.SlugField(max_length=255, unique=True)
    title = models.CharField(max_length=255, unique=True)
    image = models.FileField(upload_to="api/blog/static/img/posts/%Y_%m_%d")
    short_description = models.CharField(max_length=150, blank=True)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    status = models.BooleanField(default=True)
    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(TagPost, blank=True)
    class Meta:
        ordering = ("publish_date",)
    def __str__(self):
        return self.title
    
