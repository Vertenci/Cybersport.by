from django.forms import ModelForm

from .models import Articles


class ArlicleForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'full_text', 'img', 'date', 'game']
