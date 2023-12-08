from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib import messages

from .models import Post
from .forms import CommentCreateForm

def home(request):
    return render(request, 'base/home.html')


class PostsView(View):
    template_name = 'posts/posts.html'

    def get(self, request):
        posts = Post.objects.all()
        context = {
            'posts' : posts
        }
        return render(request, self.template_name, context=context)


class PostDetailView(View):
    template_name = 'posts/detail.html'
    form_class = CommentCreateForm

    def get(self, request, **kwargs):
        post = get_object_or_404(Post, id=kwargs['post_id'], slug=kwargs['post_slug'])
        comments = post.comments.all()
        form = self.form_class()
        context = {
            'post' : post,
            'comments' : comments,
            'form' : form
        }
        return render(request, self.template_name, context=context)
    
    def post(self, request, **kwargs):
        post = get_object_or_404(Post, id=kwargs['post_id'], slug=kwargs['post_slug'])
        form = self.form_class(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, 'You have successfully add a comment', 'success')
            return redirect(post.get_absolute_url())
        else:
            context = {
                'post' : post,
                'form' : form
             }
            return render(request, self.template_name, context=context)