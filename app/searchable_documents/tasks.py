import logging
import textract

from django.db import transaction

from celery import shared_task

from wagtail.documents import get_document_model


logger = logging.getLogger(__name__)


@shared_task()
def transcribe_document(id):
    document = get_document_model().objects.get(id=id)

    if document.transcription != "":
        print("Skipping transcription for %s" % document.filename)
        return
    
    document.transcription = "Transcribing..."
    with transaction.atomic():
        document.save(transcribe=False)

    """Store the Document file's text in the transcription field."""
    try:
        text = textract.process(document.file.path).strip()
        if not text:
            logger.debug('No text found, falling back to tesseract.')
            text = textract.process(
                document.file.path,
                method='tesseract',
            ).strip()

    except Exception as err:
        text = None
        logger.error(
            'Text extraction error with file {file}: {message}'.format(
                file=document.filename,
                message=str(err),
            )
        )

    if text:
        
        document.transcription = text.decode()
        with transaction.atomic():
            document.save(transcribe=False)
        print("Saved transcription: %s" % text)
    else:
        logger.error('No text found.')
