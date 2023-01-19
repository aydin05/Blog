from modeltranslation.translator import translator, TranslationOptions
from .models import *


class PostTranslationOptions(TranslationOptions):
    fields = ('title1', 'title2', 'content')


translator.register(Post, PostTranslationOptions)


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


translator.register(News, NewsTranslationOptions)


class AboutUsTranslationOptions(TranslationOptions):
    fields = ('name', 'title', 'text')


translator.register(AboutUs, AboutUsTranslationOptions)


class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


translator.register(Service, ServiceTranslationOptions)


class ProjectsTranslationOptions(TranslationOptions):
    fields = ['title', 'content']


translator.register(Projects, ProjectsTranslationOptions)
