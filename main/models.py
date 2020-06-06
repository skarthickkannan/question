from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField

class Post(models.Model):
    question = RichTextField(null=True, blank=True)
    date_posted =  models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes       = models.ManyToManyField(User, related_name='blog_post')
    dislikes       = models.ManyToManyField(User, related_name='blog_posts')

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('home')

    def total_likes(self):
        return self.likes.count()

    class Meta:
        ordering = ['-date_posted']

class Answer(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='answers', null=True)
    answer = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.answer

    def get_absolute_url(self):
        return reverse('home')

class Comment(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='comments', null=True)
    user = models.CharField(max_length=200)
    comments = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.user

    def get_absolute_url(self):
        return reverse('post_answer_comment', kwargs={'pk': self.pk})


