from modeltranslation.translator import register, TranslationOptions
from .models import Project, ContentBlock


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'location', 'description')


@register(ContentBlock)
class ContentBlockTranslationOptions(TranslationOptions):
    fields = ('title', 'description')