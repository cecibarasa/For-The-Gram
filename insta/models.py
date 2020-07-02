from django.db import models

# Create your models here.
class Instalite(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']

class Image(models.Model):
    name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)       

