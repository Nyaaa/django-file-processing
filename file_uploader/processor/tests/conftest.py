import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient

from ..models import File


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def uploaded_file():
    file_field = SimpleUploadedFile('text_file.txt', b'_')
    file_object = File.objects.create(file=file_field)
    yield file_object
    file_object.file.delete()
