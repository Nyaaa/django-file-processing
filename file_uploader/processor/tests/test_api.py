from unittest.mock import patch
from pathlib import Path

import pytest
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status

from ..tasks import process_file


@pytest.mark.django_db
class TestAPI:
    pytestmark = pytest.mark.django_db

    def test_get_file_list(self, client):
        response = client.get('/files/')
        assert response.status_code == status.HTTP_200_OK

    @patch.object(process_file, 'delay')  # Mock Celery
    def test_upload_file_201(self, mock_delay, client):
        file = SimpleUploadedFile('test.txt', b'file_content', content_type='text/plain')
        response = client.post('/upload/', data={'file': file}, format='multipart')
        full_path = settings.BASE_DIR / response.data['file'][1:]
        assert response.status_code == status.HTTP_201_CREATED
        assert full_path.is_file()
        Path.unlink(full_path)

    def test_upload_file_400(self, client):
        response = client.post('/upload/', data={'file': ''}, format='multipart')
        assert response.status_code == status.HTTP_400_BAD_REQUEST
