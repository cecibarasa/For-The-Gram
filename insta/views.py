from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image
from django.contrib.auth.decorators import login_required
from .forms import ImageForm, EditProfileForm


# Create your views here.
@login_required(login_url='/accounts/login/')        
def home(request):
    insta = Image.insta_today()
    return render(request, 'the-gram/index.html', {"insta": insta})

@login_required(login_url='/login')    
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.author = current_user
            image.save()
        return redirect('/')
    else:
        form = ImageForm(auto_id=False)
    return render(request, 'the-gram/new_post.html', {"form": form})
    
@login_required(login_url='/login')
def profile(request):
    # pics = Image.get_images()
    if request.method == 'POST':
        u_form = EditProfileForm(request.POST, instance=request.user)
        
        if u_form.is_valid() :
            u_form.save()
            
            
            return redirect('/profile')
    else:
        u_form = EditProfileForm(instance=request.user)
        
    return render(request, 'the-gram/profile.html', {"u_form": u_form,})       