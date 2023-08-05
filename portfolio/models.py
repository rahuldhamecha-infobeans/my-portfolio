from django.db import models
from django.utils.html import mark_safe
from django.utils.timezone import now


# Create your models here.

class PortfolioCategory(models.Model):
    name = models.CharField(blank=False,max_length=265)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    name = models.CharField(blank=False, max_length=5000)
    description = models.CharField(blank=False, max_length=5000)
    image = models.ImageField(upload_to='portfolio_images', blank=False)
    category = models.ForeignKey(PortfolioCategory,on_delete=models.CASCADE)

    # Return the service name with the object
    def __str__(self):
        return self.name

    def portfolio_image(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />' % (self.image.url))

    portfolio_image.short_description = 'Portfolio Image'
    
class Testimonial(models.Model):
    name = models.CharField(blank=False,max_length=256)
    position = models.CharField(blank=False,max_length=256)
    content = models.TextField(blank=False)

    def __str__(self):
        return self.name
    
class Subscriber(models.Model):
    email = models.CharField(blank=False,max_length=256)
    is_subscribe = models.BooleanField(default=True)

    def __str__(self):
        return self.email


class Contact(models.Model):
    name = models.CharField(blank=False,max_length=256)
    email = models.CharField(blank=False,max_length=256)
    subject = models.CharField(max_length=400)
    message = models.TextField()
    created_date = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return self.name