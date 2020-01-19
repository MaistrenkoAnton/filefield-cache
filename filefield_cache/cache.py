from django.core.files.uploadedfile import InMemoryUploadedFile
try:
    from cStringIO import StringIO as BytesIO
except ImportError:
    from io import BytesIO
from django.core.cache import caches
cache = caches['default']


class TestFileCache:

    def __init__(self):
        self.cache = cache

    def set(self, key, upload):
        state = {
            "name": upload.name,
            "size": upload.size,
            "content_type": upload.content_type,
            "charset": upload.charset,
            "content": upload.file.read()}
        upload.file.seek(0)
        self.cache.set(key, state, 20)

    def get(self, key):
        upload = None
        state = self.cache.get(key)
        if state:
            f = BytesIO()
            f.write(state["content"])
            upload = InMemoryUploadedFile(
                file=f,
                field_name='field_name',
                name=state["name"],
                content_type=state["content_type"],
                size=state["size"],
                charset=state["charset"],
            )
            upload.file.seek(0)
        return upload


class FileCache:
    """
    Cache file data and retain the file after failed validation
    """
    timeout = 1000

    def __init__(self):
        self.cache = cache

    def set(self, key, upload):
        """
        Set file data to cache for 1000s
        :param key: cache key
        :param upload: file data
        """
        try:
            state = {
                "name": upload.name,
                "size": upload.size,
                "content_type": upload.content_type,
                "charset": upload.charset,
                "content": upload.file.read()}
            upload.file.seek(0)
            self.cache.set(key, state, self.timeout)
        except AttributeError:
            pass

    def get(self, key):
        """
        Get the file data from cache using specific cache key
        :param key: cache key
        :return: File data
        """
        upload = None
        state = self.cache.get(key)
        if state:
            f = BytesIO()
            f.write(state["content"])
            upload = InMemoryUploadedFile(
                file=f,
                field_name='file',
                name=state["name"],
                content_type=state["content_type"],
                size=state["size"],
                charset=state["charset"],
            )
            upload.file.seek(0)
        return upload
