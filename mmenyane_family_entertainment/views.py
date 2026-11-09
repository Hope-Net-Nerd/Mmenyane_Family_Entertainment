from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, GalleryImage

# Create your views here.

def home(request):
   return render(request,'mmenyane/home.html')


def about(request):
   return render(request,'mmenyane/about.html')



def post_list(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'mmenyane/post_list.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, 'mmenyane/post_detail.html', {'post': post})


def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'mmenyane/gallery.html', {'images': images})