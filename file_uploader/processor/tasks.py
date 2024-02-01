import logging
from time import sleep

from celery import shared_task
from identify import identify

from .models import File

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


@shared_task
def process_file(pk):
    file_record = File.objects.get(id=pk)
    tags = identify.tags_from_path(file_record.file.path)
    if not tags:
        raise NotImplementedError('Unsupported file type.')

    if 'image' in tags:
        logger.debug(f'Processing image {file_record}')
        # Expensive operation
        sleep(10)
    elif 'text' in tags:
        logger.debug(f'Processing text file {file_record}')
        sleep(5)
    else:
        logger.info(f'Processing file {file_record}')
        sleep(20)

    file_record.processed = True
    file_record.save()
    logger.info(f'Finished processing file {file_record}')
