from django.shortcuts import render,redirect,HttpResponse, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from .models import Image,Profile,Following,Comment
from django.contrib.auth.decorators import login_required
from .forms import ImageForm, ProfileForm, EditProfileForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib import messages



# Create your views here.
@login_required(login_url='/accounts/login/')        
def home(request):
    current_user = request.user
    insta = Image.insta_today()
    image = Image.objects.all()
    users = User.objects.exclude(id=request.user.id)
    # following = Following.objects.get(current_user=request.user)
    #followers = following.users.all()
    comments = Comment.objects.all()
    comment_form = CommentForm()
    context = {
        "image":image,
        "comment_form":comment_form,
        "comments":comments,
        "users":users,
        # "followers":followers,
    }
    return render(request, 'the-gram/index.html', {"insta": insta}, context)

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
    picture = Image.get_photo()
    if request.method == 'POST':
        u_form = EditProfileForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'You have successfully updated your profile!')
            return redirect('/')
    else:
        u_form = EditProfileForm(instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
    return render(request, 'the-gram/profile.html', {"u_form": u_form, "p_form": p_form, "picture": picture})

@login_required
def likes(request, post_id):
    post = Post.objects.get(pk=post_id)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def follow(request,operation,pk):
    new_follower = User.objects.get(pk=pk)
    if operation == 'add':
        Following.make_user(request.user, new_follower)
    elif operation == 'remove':
        Following.loose_user(request.user, new_follower)

    return redirect('posts')        