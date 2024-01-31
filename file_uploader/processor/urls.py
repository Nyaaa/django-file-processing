from django.urls import path

from .views import FileListView, FileUploadView

urlpatterns = [
    path('files/', FileListView.as_view(), name='file-list'),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
]
