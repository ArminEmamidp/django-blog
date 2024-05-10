from django.contrib import admin

from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'auther', 'title', 'created', 'updated']
    list_filter = ['auther', 'title', 'created']
    search_fields = ['title', 'description', 'slug']
    # prepopulated_fields = {'slug' : ['description']} 
    # raw_id_fields = ['auther']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'auther', 'post', 'created']
    list_filter = ['auther', 'post', 'created']
    search_fields = ['auther', 'content']

