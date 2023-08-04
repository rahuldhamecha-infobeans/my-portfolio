from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=256)
    category_user = models.ForeignKey(User, related_name='category_user', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=400)
    user = models.ForeignKey(User, related_name='user', on_delete=models.DO_NOTHING)
    date = models.DateField()
    content = models.TextField()
    categories = models.ManyToManyField(Category)
    status = models.BooleanField(default=False)
    blog_image = models.ImageField(upload_to='blog_images',blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["id"]
