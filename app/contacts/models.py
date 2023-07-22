from wagtail import blocks
from wagtail.fields import StreamField
from base.models import BasePage
from wagtail.admin.panels import FieldPanel

from contacts import blocks

class ContactsPage(BasePage):
    contacts = StreamField(
        [("contacts", blocks.ContactBlock())],
        blank=True,
        use_json_field=True,
        help_text="Add contacts here",
    )

    content_panels = BasePage.content_panels + [
        FieldPanel("contacts"),
    ]
