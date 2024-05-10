from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('signout/', views.signout_view, name='signout'),
    
    path('<username>/', views.ProfileView.as_view(), name='profile'),
    path('<username>/delete/', views.delete_account_view, name='delete'),
    path('<username>/update/', views.UpdateProfileView.as_view(), name='update')
]