from django.contrib import admin
from .models import Post, Answer, Comment, Profile

admin.site.register(Post)
admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(Profile)