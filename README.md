# django-file-processing
REST API for file uploading and processing.

## Features:
* Implements two endpoints:
  * /uploads/ (POST) - upload a file
  * /files/ (GET) - get a list of all uploaded files
* API documentation:
  * Swagger available at /docs/
* File processing:
  * Tasks processed by Celery via Redis broker
  * Flower available on port 5555
  * Detect MIME type and branch processing logic based on type

