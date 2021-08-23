from django.contrib import admin
from .models import Profile, Post, TagPost

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile

@admin.register(TagPost)
class TagAdmin(admin.ModelAdmin):
    model = TagPost
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post

    list_display = (
        "id",
        "slug",
        "title",
        "publish_date",
        "status",
    )

    list_filter = (
        "status",
        "publish_date",
    )

    list_editable = (
        "slug",
        "title",
        "publish_date",
        "status",
    )
    search_fields = (
        "slug",
        "title",
        "contente",
    )
    prepopulated_fields = {
        "slug": (
            "title",
        )
    }
    date_hierarchy = "publish_date"
    save_on_top = True