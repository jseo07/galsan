from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.CharField(max_length=100, default=' ')
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, default='announcement')

    def __str__(self):
        return self.title
