from django.urls import path

from . import views

app_name = "nicepost"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("post/<int:pk>/", views.post_details_view, name="post_details"),
    path("create/post/", views.create_post_view, name="create_post"),
    path("edit/post/<int:pk>", views.edit_post_view, name="edit_post"),
    path("delet/post/<int:pk>", views.delet_post_view, name="delet_post"),
]

