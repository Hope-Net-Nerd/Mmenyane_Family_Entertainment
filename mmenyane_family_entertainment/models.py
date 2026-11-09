from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    cover_image = models.ImageField(upload_to='posts/', blank=True, null=True)
    summary = models.CharField(max_length=300, blank=True)
    body = models.TextField()
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    caption = models.CharField(max_length=200, blank=True)
    uploaded_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.caption or f'Image {self.pk}'