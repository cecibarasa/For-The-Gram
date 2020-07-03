from django.shortcuts import render
from django.http import HttpResponse
from .models import Image

# Create your views here.
def insta(request):
    insta = Image.insta_today()
    return render(request,'the-gram/index.html',{"insta":insta})