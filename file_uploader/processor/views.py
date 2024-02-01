from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import File
from .serializers import FileSerializer
from .tasks import process_file


class FileListView(ListAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all().order_by('-uploaded_at')


class FileUploadView(APIView):
    parser_classes = [MultiPartParser]
    serializer_class = FileSerializer

    def post(self, request):
        upload = self.serializer_class(data=request.data)
        if upload.is_valid():
            # Currently accepting all files as is.
            # We should only allow files we can process.
            uploaded = upload.save()
            process_file.delay(pk=uploaded.pk)
            return Response(upload.data, status=status.HTTP_201_CREATED)
        return Response(upload.errors, status=status.HTTP_400_BAD_REQUEST)
