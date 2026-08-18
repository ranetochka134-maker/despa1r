from django import forms
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline
from .models import ContentBlock, Project


class ContentBlockAdminForm(forms.ModelForm):
    class Meta:
        model = ContentBlock
        fields = "__all__"
        widgets = {
            # Разрешаем все видеоформаты
            "video": forms.FileInput(attrs={
                "accept": "video/*,video/mp4,video/quicktime,video/webm,video/x-matroska,.mp4,.mov,.webm,.mkv,.avi"
            }),
            # Разрешаем любые изображения
            "image": forms.FileInput(attrs={
                "accept": "image/*,.jpg,.jpeg,.png,.webp,.svg"
            }),
            # Разрешаем PDF и архивы
            "file": forms.FileInput(attrs={
                "accept": ".pdf,.zip,.rar,.doc,.docx"
            }),
        }


class ContentBlockInline(TranslationStackedInline):
    model = ContentBlock
    form = ContentBlockAdminForm
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
    form = ContentBlockAdminForm
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
        "description",
    )
    ordering = (
        "project",
        "order",
    )