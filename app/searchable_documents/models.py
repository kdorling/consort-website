from django.db import models
from wagtail.documents.models import Document
from wagtail.search import index

from searchable_documents.tasks import transcribe_document


class DocumentWithDate(Document):

    date = models.DateField(
        "date",
        blank=True,
        null=True,
        help_text="The date associated with the document.",
    )

    admin_form_fields = Document.admin_form_fields + (
       "date",
    )

    class Meta:
        abstract = True


class TranscriptionMixin(models.Model):
    """Mixin class with transcription field and save method."""

    transcription = models.TextField(default='', blank=True)

    class Meta:
        """Don't create a table, this model is only for subclassing."""
        abstract = True

    def save(self, **kwargs):
        """Asynchronously transcribe the file."""
        transcribe = kwargs.pop('transcribe', True)
        super(TranscriptionMixin, self).save(**kwargs)
        if transcribe:
            transcribe_document.delay(self.id)


class Document(TranscriptionMixin, DocumentWithDate):
    
    """Include transcription in search_fields."""
    search_fields = DocumentWithDate.search_fields + [
        index.SearchField('transcription', boost=10),
    ]
