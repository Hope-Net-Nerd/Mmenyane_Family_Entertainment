from django import forms


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleImageField(forms.ImageField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('widget', MultipleFileInput(attrs={'accept': 'image/*'}))
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_clean = super().clean
        if isinstance(data, (list, tuple)):
            return [single_clean(d, initial) for d in data]
        return [single_clean(data, initial)]


class BulkUploadForm(forms.Form):
    images = MultipleImageField(label='Photos')
    caption = forms.CharField(
        max_length=200,
        required=False,
        help_text='Optional. This caption is applied to every photo in this upload. '
                  'You can edit individual captions afterwards.',
    )