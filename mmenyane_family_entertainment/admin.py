from django.contrib import admin, messages
from django.shortcuts import redirect, render
from django.urls import path, reverse

from .forms import BulkUploadForm
from .models import GalleryImage, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'created_at')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'uploaded_at')
    change_list_template = 'admin/mmenyane/galleryimage/change_list.html'

    def get_urls(self):
        info = self.model._meta.app_label, self.model._meta.model_name
        custom_urls = [
            path(
                'bulk-upload/',
                self.admin_site.admin_view(self.bulk_upload),
                name='%s_%s_bulk_upload' % info,
            ),
        ]
        return custom_urls + super().get_urls()

    def bulk_upload(self, request):
        if request.method == 'POST':
            form = BulkUploadForm(request.POST, request.FILES)
            if form.is_valid():
                caption = form.cleaned_data['caption']
                files = form.cleaned_data['images']
                for f in files:
                    GalleryImage.objects.create(image=f, caption=caption)
                messages.success(request, f'{len(files)} photo(s) uploaded successfully.')
                info = self.model._meta.app_label, self.model._meta.model_name
                return redirect(reverse('admin:%s_%s_changelist' % info))
        else:
            form = BulkUploadForm()

        context = {
            **self.admin_site.each_context(request),
            'opts': self.model._meta,
            'title': 'Upload multiple photos',
            'form': form,
        }
        return render(request, 'admin/mmenyane/galleryimage/bulk_upload.html', context)