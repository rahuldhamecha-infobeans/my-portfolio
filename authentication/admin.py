from django.contrib import admin
from authentication.models import UserProfile


# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user','social_link','profile_pic_image']
    list_per_page = 10
    