from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('about/', views.about, name='about'),
   path('news/', views.post_list, name='post_list'),
   path('news/<slug:slug>/', views.post_detail, name='post_detail'),
   path('gallery/', views.gallery, name='gallery'),
]