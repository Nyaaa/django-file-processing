from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import File
from .serializers import FileSerializer


class FileListView(ListAPIView):
    serializer_class = FileSerializer
    queryset = File.objects.all()


class FileUploadView(APIView):
    parser_classes = [FormParser, MultiPartParser]
    serializer_class = FileSerializer

    def post(self, request):
        upload = self.serializer_class(data=request.data)
        if upload.is_valid():
            upload.save()
            return Response(upload.data, status=status.HTTP_201_CREATED)
        return Response(upload.errors, status=status.HTTP_400_BAD_REQUEST)
