from django.urls import path

from . import views

app_name = 'nicepost'

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('post/<int:post_id>/', views.post_details_view, name='post_details')
]

