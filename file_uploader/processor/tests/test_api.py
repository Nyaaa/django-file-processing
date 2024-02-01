import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestAPI:
    pytestmark = pytest.mark.django_db

    def test_get_file_list(self, client):
        response = client.get('/files/')
        assert response.status_code == status.HTTP_200_OK

    def test_upload_file(self, client):
        video = SimpleUploadedFile('test.txt', b'file_content', content_type='text/plain')
        response = client.post('/upload/', data={'file': video}, format='multipart')
        print(response.data)
        assert response.status_code == status.HTTP_201_CREATED
