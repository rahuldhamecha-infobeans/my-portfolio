from django.db import models
from django.utils.html import mark_safe


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