from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Image
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')        
def home(request):
    insta = Image.insta_today()
    return render(request,'the-gram/index.html',{"insta":insta})