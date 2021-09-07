from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class FreeCourses(models.Model):
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=3000)
    outcome = models.CharField(max_length=5000)
    status = models.CharField(max_length=50)
    headline = models.CharField(max_length=3000)
    uploaded = models.CharField(max_length=300)
    link = models.CharField(max_length=1000)
    category=models.CharField(max_length=200)
    image_name = models.CharField(max_length=200)
    image_url = models.CharField(max_length=500)
    image_file = models.ImageField(upload_to='images/', blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date_created']










