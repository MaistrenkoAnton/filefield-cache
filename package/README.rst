# Django Form File Field cache

Quick start
-----------

**pip install filefield-cache**

1. Add **material.admin** and **material.admin.default** to your INSTALLED_APPS setting instead of **filefield_cache**::
 - required

.. code-block:: python

    INSTALLED_APPS = (
        ...

        'filefield_cache',
        ...
    )


2. Add Admin form in **admin.py**
 - required
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
 - required
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
