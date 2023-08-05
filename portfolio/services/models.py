from django.db import models
from django.utils.html import mark_safe


# Create service models for storing services
class Service(models.Model):
    service_name = models.CharField(blank=False, max_length=5000)
    service_description = models.CharField(blank=False, max_length=5000)
    service_image = models.ImageField(upload_to='service_images', blank=False)

    # Return the service name with the object
    def __str__(self):
        return self.service_name

    def service_image_tag(self):
        return mark_safe('<img src="%s" width="100px" height="100px" />' % (self.service_image.url))

    service_image_tag.short_description = 'Service Image'
