from wagtail import blocks


class ContactBlock(blocks.StructBlock):
    name = blocks.CharBlock(required=True, help_text="Enter the name of the profile")
    position = blocks.RichTextBlock(required=True, help_text="Enter the position of the profile")
    email = blocks.EmailBlock(required=True, help_text="Enter the email of the profile")
    phone = blocks.CharBlock(required=True, help_text="Enter the location of the profile")

    class Meta:
        template = "contacts/blocks/contact_block.html"
        icon = "user"
        label = "Contact"
