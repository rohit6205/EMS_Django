from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.TextField(null=True, blank=True)
    status = models.CharField(default='inactive', max_length=10)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE) 

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.ForeignKey('polls.Question', on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class 