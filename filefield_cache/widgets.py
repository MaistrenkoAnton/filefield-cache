import hashlib

from django.contrib.admin.widgets import AdminFileWidget

from filefield_cache.cache import FileCache


class CachedAdminFileWidget(AdminFileWidget):
    """
    Put the file data into the cache for retaining
    """
    template_name = 'filefield_cache/cached_clearable_file_input.html'
    format_cache_key = '{}-cached-filefield'
    cache = FileCache()

    def value_from_datadict(self, data, files, name):
        """
        Put the file from cache into data
        :param data: Form data
        :param files: FILES data
        :param name: Field name
        """
        if not files.get(name):
            field_name = self.format_cache_key.format(name)
            _hash = data.get(field_name)
            if data.get(f'{name}-clear-cache'):
                self.cache.delete(_hash)
            else:
                files = self._get_cache_files(_hash, files, name)
        return super().value_from_datadict(data, files, name)

    def _get_cache_files(self, _hash, files, name):
        """
        Return prepared files data
        :param _hash: cache key
        :param files: files from form
        :param name: field name
        :return: prepared files data
        """
        file = self.cache.get(_hash)
        if file:
            files = {name: file}
        return files

    def get_context(self, name, value, attrs):
        """
        Extend widget template context
        """
        _hash = None
        if value:
            _hash = hashlib.md5(value.read()).hexdigest()
            value.seek(0)
            self.cache.set(_hash, value)
        context = super().get_context(name, value, attrs)
        context['widget'].update({
            'hash': _hash,
            'file_name': value,
        })
        return context
