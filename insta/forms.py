from .models import Image,Profile,User,Comment
from django import forms

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['comments', 'likes']
        

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class EditProfileForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo', 'bio']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']               
        
               