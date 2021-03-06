from django.contrib import admin

from .models import Language ,Snippet


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass

@admin.register(Snippet)

class SnippetAdmin(admin.ModelAdmin):
    pass

