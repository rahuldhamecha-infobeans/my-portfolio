from django.db import models


# Create service models for storing services
class Service(models.Model):
    service_name = models.CharField(blank=False, max_length=4000)
    service_description = models.CharField(blank=False, max_length=4000)
    service_image = models.ImageField(upload_to='service_images', blank=False)

    # Return the service name with the object
    def __str__(self):
        return self.service_name
