from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class PostModel(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE , default= None)
    date_created = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ('-date_created',)
    
    def __str__(self):
        return self.title
