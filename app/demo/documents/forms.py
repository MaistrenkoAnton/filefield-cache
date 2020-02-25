from django import forms

from filefield_cache.widgets import CachedAdminFileWidget
from demo.documents.models import Document


class DocumentForm(forms.ModelForm):
    file = forms.FileField(widget=CachedAdminFileWidget, required=False)
    picture = forms.ImageField(widget=CachedAdminFileWidget, required=False)

    class Meta:
        model = Document
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if name == 'test':
            raise forms.ValidationError('Invalid value', code='invalid')
        return name
