from wagtail.documents.forms import BaseDocumentForm

from wagtail.admin.widgets.datetime import AdminDateInput


class DocumentWithDateForm(BaseDocumentForm):
    class Meta(BaseDocumentForm.Meta):
        widgets = {"date": AdminDateInput}
