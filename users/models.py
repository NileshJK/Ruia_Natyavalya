from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Upload_File = models.FileField()

    def __str__(self):
        return f'{self.user} Profile'