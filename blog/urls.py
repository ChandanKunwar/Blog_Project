from django.urls import path
from django.urls.resolvers import URLPattern
from .import views

urlpatterns = [
    path('blog/',views.index,name='index'),
    path('post_detail/<int:pk>/', views.post_detail, name='blog-post-detail'),
    path('post_edit/<int:pk>/', views.post_edit, name='blog-post-edit'),
    path('post_delet/<int:pk>/', views.post_delet, name='blog-post-delet'),
]