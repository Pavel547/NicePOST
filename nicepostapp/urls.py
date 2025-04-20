from django.urls import path

from . import views

app_name = "nicepost"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("post/<int:pk>/", views.post_details_view, name="post_details"),
    path("add_post/", views.addpost_view, name="add_post"),
]

