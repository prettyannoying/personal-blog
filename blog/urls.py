from django.urls import path
from .views import (PostListView, 
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView)
from . import views
from .models import Post

urlpatterns = [
	#path(r'^tinymce/',include('tinymce.urls')),
	path('',PostListView.as_view(),name='blog-home'),
	#path('post/<slug:slug>/',PostDetailView.as_view(),name='post-details'),
	path('post/<slug:slug>/',PostDetailView.as_view(),name='post-detail'),
	path('post/new',PostCreateView.as_view(),name='post-create'),
	path('post/<slug:slug>/update',PostUpdateView.as_view(),name='post-update'),
	path('post/<slug:slug>/delete',PostDeleteView.as_view(),name='post-delete'),
	path('about/',views.about, name='blog-about'),
]
