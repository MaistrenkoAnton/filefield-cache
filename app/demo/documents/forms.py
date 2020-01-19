from django import forms

from filefield_cache.widgets import CachedAdminFileWidget, TestCachedAdminFileWidget
from demo.documents.models import Document


class DocumentForm(forms.ModelForm):
    file = forms.FileField(widget=CachedAdminFileWidget)
    picture = forms.ImageField(widget=CachedAdminFileWidget)

    class Meta:
        model = Document
        fields = '__all__'
