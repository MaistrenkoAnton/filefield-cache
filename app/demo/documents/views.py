from django.views.generic.edit import CreateView

from demo.documents.forms import DocumentForm


class DocumentView(CreateView):
    template_name = 'documents/form.html'
    form_class = DocumentForm
    success_url = '/admin/'
