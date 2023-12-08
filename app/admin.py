from django.contrib import admin

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'user', 'created', 'updated']
    list_filter = ['title', 'user', 'created', 'updated']
    search_fields = ['title', 'user']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'created']
    list_filter = ['user_name', 'created']
    search_fields = ['user_name', 'body']