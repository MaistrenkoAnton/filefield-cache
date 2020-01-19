import hashlib

from django.contrib.admin.widgets import AdminFileWidget

from filefield_cache.cache import FileCache, TestFileCache


class TestCachedAdminFileWidget(AdminFileWidget):
    def value_from_datadict(self, data, files, name):
        if not files.get(name):
            files = {name: FileCache().get('123')}
        upload = super().value_from_datadict(data, files, name)
        return upload

    def get_context(self, name, value, attrs):
        if value:
            FileCache().set('123', value)
        context = super().get_context(name, value, attrs)
        context['widget'].update({
            'file_name': value,
        })
        return context


class CachedAdminFileWidget(AdminFileWidget):
    """
    Put the file data into the cache for retaining
    """
    template_name = 'filefield_cache/cached_clearable_file_input.html'
    format_cache_key = '{}-cached-filefield'

    def value_from_datadict(self, data, files, name):
        if not files.get(name):
            field_name = self.format_cache_key.format(name)
            _hash = data.get(field_name)
            files = {name: FileCache().get(_hash)}
        return super().value_from_datadict(data, files, name)

    def get_context(self, name, value, attrs):
        _hash = None
        if value:
            _hash = hashlib.md5(value.read()).hexdigest()
            value.seek(0)
            FileCache().set(_hash, value)
        context = super().get_context(name, value, attrs)
        context['widget'].update({
            'hash': _hash,
            'file_name': value,
        })
        return context
