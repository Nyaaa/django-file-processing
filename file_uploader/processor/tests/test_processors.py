import pytest

from ..tasks import process_file


@pytest.mark.django_db
class TestFileProcessors:
    pytestmark = pytest.mark.django_db

    def test_process_text_file(self, uploaded_file):
        assert uploaded_file.processed is False
        process_file(pk=1)
        uploaded_file.refresh_from_db()
        assert uploaded_file.processed is True
