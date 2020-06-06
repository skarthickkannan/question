"""que URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from main.views import home, PostList, PostDetailView, PostCreateView, search, AnswerCreateView, CommentCreateView, like_view, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostList.as_view(template_name='home.html'), name='home'),
    path('search/', search, name='search'),
    path('like/<int:pk>/', like_view, name='like_post'),
    path('post/<int:pk>/detail/', PostDetailView.as_view(template_name='post_detail.html'), name='post_detail'),
    path('post/new/', PostCreateView.as_view(template_name='post_form.html'), name='post'),
    path('post/<int:id>/detail/answer/', AnswerCreateView, name='post_answer'),
    path('post/<int:id>/detail/answer/comment/', CommentCreateView, name='post_answer_comment'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),


]
