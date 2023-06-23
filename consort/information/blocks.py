from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.blocks import RichTextBlock


class Link(blocks.StructBlock):
    link_text = blocks.CharBlock(
        max_length=50,
        default="More Details"
    )
    internal_page = blocks.PageChooserBlock(
        required=False
    )
    external_link = blocks.URLBlock(
        required=False
    )


class Card(blocks.StructBlock):
    title = blocks.CharBlock(
        max_length=100,
        help_text="Bold title text for this card. Max length of 100 characters."
    )
    text = blocks.TextBlock(
        max_length=255,
        help_text="Optional text for this card. Max length is 255 characters.",
        required=False
    )
    image = ImageChooserBlock(
        help_text="Image will be automatically cropped to 570px x 370px"
    )
    link = Link(
        help_text="Enter a link or select a page"
    )


class CardsBlock(blocks.StructBlock):
    cards = blocks.ListBlock(
        Card()
    )

    class Meta:
        template = "information/blocks/cards_block.html"
        icon = "image"
        label = "Standard Cards"
        help_text = "A set of cards on the page"


class ImageAndTextBlock(blocks.StructBlock):
    image = ImageChooserBlock(
        required=True,
        help_text="Image automatically cropped to 786px by 552px"
    )
    image_alignment = blocks.ChoiceBlock(
        choices=(
            ("left", "Image to the left"),
            ("right", "Image to the right")
        ),
        default="left", 
        help_text="Image on one side of the screen, with text on the other"
    )
    title = blocks.CharBlock(max_length=60, help_text="Max length of 60 characters.")
    text = blocks.CharBlock(max_length=140, required=False)
    link = Link()

    class Meta:
        template = "information/blocks/image_and_text_block.html"
        icon = "image"
        label = "Image & Text"


class GenericSectionValue(blocks.StructValue):
    def anchor(self):
        header = self.get("header")
        return f"{header.lower().replace(' ', '_')}"


class GenericSectionBlock(blocks.StructBlock):
    common_sections = [
        ("cards", CardsBlock()),
        ("image_and_text", ImageAndTextBlock()),
        ("text", RichTextBlock()),
    ]

    header = blocks.CharBlock(
        required=True,
        help_text="The section's title",
    )

    content = blocks.RichTextBlock(
        required=True,
        help_text="The section's content",
    )

    class Meta:
        icon = "edit"
        value_class = GenericSectionValue


class SubSubSectionBlock(GenericSectionBlock):
    
    subcontent = blocks.StreamBlock(
        GenericSectionBlock.common_sections,
        required=False,
        help_text="The subsubsection's subcontent"
    )

    class Meta:
        template = "information/blocks/subsubsection_block.html"
        label = "SubSubSection"
        help_text = "A subsubsection of the document"


class SubSectionBlock(GenericSectionBlock):  

    subcontent = blocks.StreamBlock(
        GenericSectionBlock.common_sections + [("subsubsection", SubSubSectionBlock())],
        required=False,
        help_text="The subsection's content"
    )

    class Meta:
        template = "information/blocks/subsection_block.html"
        label = "SubSection"
        help_text = "A subsubsection of the document"


class SectionBlock(GenericSectionBlock):

    subcontent = blocks.StreamBlock(
            GenericSectionBlock.common_sections + [("subsection", SubSectionBlock())],
            required=False,
            help_text="The section's content"
        )
    
    class Meta:
        template = "information/blocks/section_block.html"
        label = "Section"
        help_text = "A section of the document"