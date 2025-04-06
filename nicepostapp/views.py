from django.shortcuts import render, redirect

from . import models

def home_view(request):
    posts = models.Post.objects.all()
    return render(request, "nicepostapp/index.html", {'post_list': posts})

def post_details_view(request, post_id):
    post = models.Post.objects.get(pk=post_id)
    return render(request, "nicepostapp/post_detail.html", {'post': post})
