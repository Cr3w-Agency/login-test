from django.contrib import admin
from .models import Author, News

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(News)