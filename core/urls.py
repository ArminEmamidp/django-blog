"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import global_settings
from django.shortcuts import render

# index view
def home(request):
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'), # This is home view

    path('blog/', include('blog.urls', namespace='blog')),
    path('account/', include('account.urls', namespace='account')),

    path('froala_editor/', include('froala_editor.urls')) # The editor for create content of blog posts
]

if global_settings.DEBUG:
    urlpatterns += static(global_settings.STATIC_URL, document_root=global_settings.STATIC_ROOT),
    urlpatterns += static(global_settings.MEDIA_URL, document_root=global_settings.MEDIA_ROOT),