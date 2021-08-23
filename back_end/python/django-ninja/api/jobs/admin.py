from django.contrib import admin
from .models import Company, Jobs, TagJobs


# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    model = Company

@admin.register(TagJobs)
class TagAdmin(admin.ModelAdmin):
    model = TagJobs

@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
    model = Jobs

    list_display = (
        "id",
        "slug",
        "title",
        "workplace",
        "description",
        "status",
    )
    list_filter = (
        "status",
        "date_created",
    )
    list_editable = (
        "title",
        "workplace",
        "description",
        "status",
    )
    search_fields = (
        "slug",
        "title",
        "workplace",
        "description",
    )
    prepopulated_fields = {
        "slug": (
            "title",
            "workplace",
        )
    }
    date_hierarchy = "date_created"
    save_on_top = True