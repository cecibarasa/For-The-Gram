from .models import Image,Profile,User
from django import forms

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'likes']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class EditProfileForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
        
               