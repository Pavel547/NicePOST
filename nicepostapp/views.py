from django.shortcuts import render, redirect, get_object_or_404

from . import models
from .forms import PostForm, CommentForm, ImgForm
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView

def home_view(request):
    posts = models.Post.objects.all()
    template = "index.html"
    return render(request, template, {'post_list': posts})

def post_details_view(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    template = 'posts/post_detail.html'
    if request.method == "POST":
        comment = CommentForm(request.POST)
        if comment.is_valid():
            newcomment = comment.save(commit=False)
            newcomment.post = post
            newcomment.save()
    else:
        comment = CommentForm()
        
    context = {
        "post": post,
        "comment": comment,
    }
    return render(request, template, context)

@login_required
def create_post_view(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        img = ImgForm(request.POST, request.FILES)
        if form.is_valid() and img.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            postimg = img.save(commit=False)
            postimg.imgs = post
            postimg.save()
   
            return redirect("nicepost:home")
    else:
        form = PostForm()
        img = ImgForm()
    
    context = {
        "postform": form,
        "imgform": img,
    }
    return render(request, "posts/post_form.html", context)

class EdittePost(UpdateView):
    model = models.Post
    fields = ["title", "content"]
    template_name = "post_edit.html"
    success_url = "nicepost:home"

def edit_post_view(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("nicepost:home")
    else:
        form = PostForm(instance=post)
    context = {
        "editform": form,
    }
    return render(request, "posts/post_edit.html", context)
    
def delet_post_view(request, pk):
    post = models.Post.objects.get(id=pk)
    post.delete()
    return redirect("nicepost:home")
    