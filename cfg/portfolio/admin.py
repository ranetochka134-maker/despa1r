from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline
from .models import ContentBlock, Project


class ContentBlockInline(TranslationStackedInline):
    model = ContentBlock
    extra = 1
    ordering = ("order",)


@admin.register(Project)
class ProjectAdmin(TabbedTranslationAdmin):
    list_display = (
        "title",
        "category",
        "year",
        "location",
    )

    list_filter = (
        "category",
        "year",
    )

    search_fields = (
        "title",
        "description",
    )

    inlines = [
        ContentBlockInline,
    ]


@admin.register(ContentBlock)
class ContentBlockAdmin(TabbedTranslationAdmin):
    list_display = (
        "project",
        "content_type",
        "title",
        "order",
    )

    list_filter = (
        "content_type",
        "project",
    )

    search_fields = (
        "title",
        "text",
    )

    ordering = (
        "project",
        "order",
    )