from django.db import models
from django.contrib.auth.models import User

# Create user profile models for storing user profiles pic
class UserProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    social_link = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    # Return the user name with the object
    def __str__(self):
        return self.user.username
