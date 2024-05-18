from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages

from .models import Post, Comment
from .forms import CommentForm, PostSearchForm, CommentReplyForm


def posts_view(request):
    form = PostSearchForm()
    posts = Post.objects.all()

    if request.GET.get('search_text'):
        posts = posts.filter(title__contains=request.GET['search_text'])

    return render(request, 'blog/posts.html', {'posts' : posts, 'form' : form})


class PostDetailView(View):
    template_name = 'blog/detail.html'
    form_class = CommentForm
    form_class_2 = CommentReplyForm

    def setup(self, request, *args, **kwargs):
        self.post_instance = get_object_or_404(Post, id=kwargs['id'], slug=kwargs['slug'])
        return super().setup(request, *args, **kwargs)
    
    def get(self, request, **kwargs):
        form = self.form_class()
        form_2 = self.form_class_2()
        post = self.post_instance
        comments = post.comments.all().filter(is_reply=False)

        return render(request, self.template_name, {'post' : post, 'form' : form, 'comments' : comments,
                                                    'form_2' : form_2})
    
    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        post = self.post_instance
        comments = post.comments.all()

        if not request.user.is_authenticated:
            messages.error(request, 'For posting comment, you must signed in.', 'danger')
            return redirect(post.post_detail())

        if form.is_valid():
            cd = form.cleaned_data
            comment = Comment.objects.create(auther=request.user, post=post, content=cd['content'])
            comment.save()
            messages.success(request, 'You have successfully posted a comment.', 'info')
            return redirect(post.post_detail())
        return render(request, self.template_name, {'post' : post, 'form' : form, 'comments' : comments})


def post_comment_reply_view(request, id, slug, c_id):
    post = get_object_or_404(Post, id=id, slug=slug)
    comment = get_object_or_404(Comment, id=c_id)
    form = CommentReplyForm(request.POST)
    if not request.user.is_authenticated:
        return redirect('home')
    if form.is_valid():
        cd = form.cleaned_data
        Comment.objects.create(auther=request.user, post=post, content=cd['content'], is_reply=True, reply=comment)
        messages.success(request, 'You have replied a comment', 'info')
    return redirect(post.post_detail())
