from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name="blog-home"),
    path('about/', about, name="blog-about"),
    path('post/new', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
]
