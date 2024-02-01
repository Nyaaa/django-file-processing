from django.core.files.uploadedfile import SimpleUploadedFile

from ..models import File


def test_file_model():
    file_field = SimpleUploadedFile('text_file.txt', b'_')
    test_object = File(file=file_field)
    assert str(test_object) == 'text_file.txt'
