from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.posts_view, name='posts'),
    path('<id>/<slug>/', views.PostDetailView.as_view(), name='post_detail'),
]