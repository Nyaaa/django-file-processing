import logging
from time import sleep

import filetype
from celery import shared_task

from .models import File

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


@shared_task
def process_file(pk):
    file_record = File.objects.get(id=pk)
    file_actual = file_record.file
    logger.info(f'Processing file {file_record}')

    # Expensive operation
    sleep(10)

    _filetype = filetype.guess(file_actual)
    file_record.processed = True
    file_record.save()
    logger.info(f'Finished processing file {file_record}')
    logger.debug(f'Filetype detected: {_filetype.mime}')
