from django.contrib import admin
from django.contrib.admin import register

from demo.documents.forms import DocumentForm
from demo.documents.models import Document


@register(Document)
class DocumentAdmin(admin.ModelAdmin):
    form = DocumentForm
    list_display = ['name', 'file', 'picture']
