from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# create a model for the user profile
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    profile_picture = models.ImageField(upload_to='media/', blank=True)
    biography = models.TextField(blank=True)

    def __str__(self):
        return self.user.username