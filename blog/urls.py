from django.urls import path
from . import views
from .views import PostListView,DetailListView,CreateListView,UpdateListView,DeleteListView,UserPostListView
urlpatterns = [
    path('',PostListView.as_view(),name='blog-home'),
    path('user/<str:username>',UserPostListView.as_view(),name='user-posts'),
    path('post/<int:pk>/',DetailListView.as_view(),name='post-detail'),
    path('post/new/',CreateListView.as_view(),name='post-create'),
    path('post/<int:pk>/update',UpdateListView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/',DeleteListView.as_view(),name='post-delete'),
    path('about/',views.about,name='blog-about'),
]