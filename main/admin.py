from django.contrib import admin
from .models import Post, Answer, Comment

admin.site.register(Post)
admin.site.register(Answer)
admin.site.register(Comment)