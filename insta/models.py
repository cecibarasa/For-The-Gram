from django.db import models
from django.contrib.auth.models import User
import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.models import CloudinaryField



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='pictures/')
    bio = models.TextField()

    def __str__(self):
        return self.user

class Image(models.Model):
    photo =CloudinaryField('photo')
    name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=50)
    profile = models.ForeignKey(Profile, on_delete =models.CASCADE)
    likes = models.IntegerField(default=0)
    comment = models.TextField()
    # author = models.ForeignKey(User, on_delete=models.CASCADE, default='1')

    def save_image(self):
        self.save()

    def __str__(self):
        return self.name    

    @classmethod
    def insta_today(cls):
        insta = cls.objects.filter()
        return insta