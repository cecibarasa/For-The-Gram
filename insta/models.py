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
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    # comment = models.TextField()
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
    def get_photo(cls, image_id):
        insta = cls.objects.get(id =image_id)
        return insta

    def addlikes(self):
        self.likes.count()

    @classmethod
    def search_by_username(cls,search_term):
        insta = cls.objects.filter(author__username__icontains=search_term)
        return insta
        
    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update_image()

    def update_caption(self, caption):
        self.image_caption = caption
        self.save()    
class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)



    def __str__(self):
        return f'{self.image.author}, {self.user.username}'
    @classmethod
    def get_comments(cls):
        comments = Comment.objects.all()
        return comments
    def save_comment(self):
        self.save()
  


class Following(models.Model):
    users = models.ManyToManyField(User, related_name='friend_set')
    current_user = models.ForeignKey(User, related_name='owner', on_delete=models.PROTECT, null=True)

    @classmethod
    def make_user(cls,current_user,new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def loose_user(cls,current_user,new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)              