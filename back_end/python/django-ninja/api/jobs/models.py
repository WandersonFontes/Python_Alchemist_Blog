from django.db import models
from django.conf import settings

# Create your models here.
class Company(models.Model):
    admin = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    company_name =  models.CharField(max_length=255, unique=True)
    cnpj = models.CharField(max_length=50, unique=True)
    website = models.URLField(blank=True)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.admin.get_username()

class TagJobs(models.Model):
    title = models.CharField(max_length=50, unique=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Jobs(models.Model):
    class Meta:
        ordering = ["-date_created"]

    slug = models.SlugField(max_length=255, unique=True)
    title = models.CharField(max_length=255, unique=True)
    workplace = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    requirements = models.TextField()
    remote = models.BooleanField(default=False)
    meta_description = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    tags = models.ManyToManyField(TagJobs, blank=True)