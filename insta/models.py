from django.db import models
from django.contrib.auth.models import User
import cloudinary
import cloudinary.uploader
from cloudinary.models import CloudinaryField
from django.core.exceptions import ObjectDoesNotExist



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='pictures/',blank=True)
    bio = models.TextField()

    def save_profile(self):
        self.save()

    def __str__(self):
        return f'{self.user.username} Profile'

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        self.update_profile()

    @classmethod
    def get_by_id(cls, id):
        user_images = Profile.objects.filter(user=id).first()
        return user_images
    

class Image(models.Model):
    photo = CloudinaryField('photo')
    name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=50)
    profile = models.ForeignKey(Profile, on_delete =models.CASCADE, default = '1')
    likes = models.IntegerField(default=0)
    comment = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='1')

    def save_image(self):
        self.save()

    def __str__(self):
        return f'{self.profile.user.username}'  

    @classmethod
    def insta_today(cls):
        insta = cls.objects.filter()
        return insta

    @classmethod
    def get_photo(cls):
        insta = cls.objects.filter()
        return insta

    def addlikes(self):
        self.likes.count()      