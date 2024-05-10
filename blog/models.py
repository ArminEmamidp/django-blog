from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from froala_editor.fields import FroalaField


class Post(models.Model):
    auther = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField()
    content = FroalaField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
    
    def post_detail(self):
        return reverse('blog:post_detail', args=[self.id, self.slug])

    def post_like(self):
        return reverse('blog:post_like', args=[self.id, self.slug])


class Comment(models.Model):
    auther = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']


class Like(models.Model):
    auther =models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    created = models.DateTimeField(auto_now_add=True)
    