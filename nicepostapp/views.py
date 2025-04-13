from django.shortcuts import render, redirect, get_object_or_404

from . import models
from .forms import PostForm, CommentForm, ImgForm
from django.contrib.auth.models import User

def home_view(request):
    posts = models.Post.objects.all()
    template = "index.html"
    return render(request, template, {'post_list': posts})

def post_details_view(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    template = "posts/post_detail.html"
    if request.method == "POST":
        comment = CommentForm(request.POST)
        if comment.is_valid():
            newcomment = comment.save(commit=False)
            newcomment.post = post
            newcomment.user = request.user
            newcomment.save()
    else:
        comment = CommentForm()
    context = {
        "post": post,
        "comment": comment,
    }    
        
    return render(request, template, context)

def createpost_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        img = ImgForm(request.POST, request.FILES)
        if form.is_valid() and img.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            postimg = img.save(commit=False)
            postimg.imgs = post
            postimg.save()
   
            return redirect('nicepost:home')
    else:
        form = PostForm()
        img = ImgForm()

    return render(request, "posts/post_form.html", {'postform': form, 'imgform': img,})
