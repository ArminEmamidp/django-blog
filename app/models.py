from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from froala_editor.fields import FroalaField

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=70)
    description = models.TextField()
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='posts/images/')
    content = FroalaField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('app:post_detail', args=[self.pk, self.slug])


class Comment(models.Model):
    user_name = models.CharField(max_length=30)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']