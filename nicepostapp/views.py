from django.shortcuts import render, redirect

from . import models
from .forms import PostCreationForm, ImgsForm, VideoForm

def home_view(request):
    posts = models.Post.objects.all()
    return render(request, "nicepostapp/index.html", {'post_list': posts})

def post_details_view(request, post_id):
    post = models.Post.objects.get(pk=post_id)
    return render(request, "nicepostapp/post_detail.html", {'post': post})

def create_post_view(request):
    if request.method == 'POST':
        post_form = PostCreationForm(request.POST)
        imgs_form = ImgsForm(request.POST, request.FILES)
        video_form = VideoForm(request.POST, request.FILES)
        
        if post_form.is_valid() and imgs_form.is_valid and video_form.is_valid:
            post = post_form.save()
            
            img = imgs_form.save(commit=False)
            video = video_form.save(commit=False)
            img.imgs = post
            video.video = post
            
            video.save()
            img.save()
            
            return redirect("nicepost:home")
    else:
        post_form = PostCreationForm()
        imgs_form = ImgsForm()
        video_form = VideoForm() 
    
    return render(request, "nicepostapp/posts/post_form.html", {'post_form': post_form, 'imgs_form': imgs_form, 'video_form': video_form})
        