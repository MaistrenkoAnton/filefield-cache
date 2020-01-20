# Django Form File Field cache

Quick start
-----------

1. Add **filefield_cache**  INSTALLED_APPS settings:

    .. code-block:: python

        INSTALLED_APPS = (
            ...

            'filefield_cache',
            ...
        )


2. Add Admin form in **admin.py**
    .. code-block:: python

        from django.contrib import admin
        from django.contrib.admin import register

        from demo.documents.forms import DocumentForm
        from demo.documents.models import Document


        @register(Document)
        class DocumentAdmin(admin.ModelAdmin):
            form = DocumentForm
            ...


3. Create form in **forms.py**.
    .. code-block:: python

        from django import forms

        from filefield_cache.widgets import CachedAdminFileWidget
        from demo.documents.models import Document


        class DocumentForm(forms.ModelForm):
            file = forms.FileField(widget=CachedAdminFileWidget)
            picture = forms.ImageField(widget=CachedAdminFileWidget)

            class Meta:
                model = Document
                fields = '__all__'
