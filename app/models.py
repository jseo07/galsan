from django.db import models

# Create your models here.
class Usr(models.Model):
    usrname = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    dob = models.CharField(max_length=8)
    phoneno = models.CharField(max_length=11, default='010')
    phoneverified = models.BooleanField(default=False)

    USERNAME_FIELD = 'usrname'

    def __str__(self):
        return self.usrname