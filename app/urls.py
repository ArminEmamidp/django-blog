from django.urls import path

from . import views



app_name = 'app'
urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.PostsView.as_view(), name='posts'),
    path('posts/<post_id>/<post_slug>/', views.PostDetailView.as_view(), name='post_detail')
]