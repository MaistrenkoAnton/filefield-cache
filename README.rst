|pypi| |python| |django|

.. .. |build|

.. |pypi| image:: https://d25lcipzij17d.cloudfront.net/badge.svg?id=py&type=6&v=0.0.2&x2=0
    :target: https://pypi.org/project/filefield-cache/
.. |python| image:: https://img.shields.io/badge/python-3.6+-blue.svg
    :target: https://www.python.org/
.. |django| image:: https://img.shields.io/badge/django-3.0+-mediumseagreen.svg
    :target: https://www.djangoproject.com/ 

===========================================
FileField Cache For Files retaining in form
===========================================

Retain files after form validation. Keep the file data in the cache for 15 minutes and allow to resubmit form and cache data will be saved in to the database after success form validation.

.. image:: https://raw.githubusercontent.com/MaistrenkoAnton/filefield-cache//master/app/demo/screens/form.png

Cache data can be cleared by checkbox.


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
