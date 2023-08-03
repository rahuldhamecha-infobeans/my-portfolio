from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe

# Create user profile models for storing user profiles pic
class UserProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)

    social_link = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    # Return the user name with the object
    def __str__(self):
        return self.user.username

    def profile_pic_image(self):
        if self.profile_pic:
            return mark_safe('<img src="%s" width="100px" height="100px" />' % (self.profile_pic.url))
        else:
            return 'No Profile Pic'

    profile_pic_image.short_description = 'Profile Pic'
