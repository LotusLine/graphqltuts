from django.contrib import admin

from .models import *

class AuthorManager(admin.ModelAdmin):
    list_display = ('id', 'name')

class BookManager(admin.ModelAdmin):
    list_display = ('id', 'title')



admin.site.register(Author, AuthorManager)
admin.site.register(Book, BookManager)
