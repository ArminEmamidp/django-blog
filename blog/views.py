from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages

from .models import Post, Comment
from .forms import CommentForm, PostSearchForm


def posts_view(request):
    form = PostSearchForm()
    posts = Post.objects.all()

    if request.GET.get('search_text'):
        posts = posts.filter(title__contains=request.GET['search_text'])

    return render(request, 'blog/posts.html', {'posts' : posts, 'form' : form})


class PostDetailView(View):
    template_name = 'blog/detail.html'
    form_class = CommentForm

    def setup(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(Post, id=kwargs['id'], slug=kwargs['slug'])
        return super().setup(request, *args, **kwargs)
    
    def get(self, request, **kwargs):
        form = self.form_class()
        post = self.post_instance
        comments = post.comments.all()

        return render(request, self.template_name, {'post' : post, 'form' : form, 'comments' : comments})
    
    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        post = self.post_instance
        comments = post.comments.all()

        if not request.user.is_authenticated:
            messages.error(request, 'For posting comment, you must sign in.', 'danger')
            return redirect(post.post_detail())

        if form.is_valid():
            cd = form.cleaned_data
            comment = Comment.objects.create(auther=request.user, post=post, content=cd['content'])
            comment.save()
            messages.success(request, 'You have successfully posted a comment.', 'info')
            return redirect(post.post_detail())
        return render(request, self.template_name, {'post' : post, 'form' : form, 'comments' : comments})

