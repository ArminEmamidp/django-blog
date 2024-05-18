from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.posts_view, name='posts'),
    path('<id>/<slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<id>/<slug>/<c_id>/', views.post_comment_reply_view, name='post_comment_reply')
]