from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    user = models.ForeignKey(User,related_name='question_user',on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=120)