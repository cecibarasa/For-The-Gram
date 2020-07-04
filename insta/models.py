from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Instalite(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField()

#     def __str__(self):
#         return self.first_name

#     def save_instalite(self):
#         self.save()    

#     class Meta:
#         ordering = ['first_name']

class Image(models.Model):
    name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)
    comment = models.TextField()

    def save_image(self):
        self.save()

    def __str__(self):
        return self.name    

    @classmethod
    def insta_today(cls):
        insta = cls.objects.filter()
        return insta

class Profie(models.Model):
    profile_photo = models.ImageField(upload_to='pictures/')
    bio = models.TextField()