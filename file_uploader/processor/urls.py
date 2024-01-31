from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import FileListView, FileUploadView

router = DefaultRouter()

urlpatterns = [
    path('files/', FileListView.as_view(), name='file-list'),
    path('upload/', FileUploadView.as_view(), name='file-upload'),
]

urlpatterns += router.urls
