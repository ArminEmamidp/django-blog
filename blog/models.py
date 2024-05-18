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
    auther = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True)
    content = models.TextField(max_length=2000, null=True)
    is_reply = models.BooleanField(default=False, null=True)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, related_name='replies', null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-created']

    def comment_reply(self):
        return reverse('blog:post_comment_reply', args=[self.post.id, self.post.slug, self.id])
