from wagtail import blocks
from wagtail.admin import widgets
from wagtail.images.blocks import ImageChooserBlock

from base.models import BasePage


class TitleBlock(blocks.StructBlock):
    text = blocks.CharBlock(
        required=True,
        help_text="Text to display",
    )

    class Meta:
        template = "common/title_block.html"
        icon = "edit"
        label = "Title"
        help_text= "Centered text to display on the page"


class BasePageChooserBlock(blocks.PageChooserBlock):
    target_model = BasePage
    widget = widgets.AdminPageChooser()


class Link(blocks.StructBlock):
    link_text = blocks.CharBlock(
        max_length=50,
        default="More Details"
    )
    page = BasePageChooserBlock(
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


class ButtonsBlock(blocks.StructBlock):
    links = blocks.ListBlock(
        Link()
    )

    button_styles = blocks.CharBlock(
        required=False,
        max_length=150,
        help_text="Tailwind classes to style the buttons"
    )

    class Meta:
        template = "common/buttons_block.html"
        icon = "image"
        label = "Links"
        help_text = "A set of buttons on the page"


class PagesBlock(blocks.StructBlock):

    links = blocks.ListBlock(
        Link()
    )

    class Meta:
        template = "common/pages_block.html"
        icon = "image"
        label = "Pages"
        help_text = "A set of pages"


class PopularPagesBlock(blocks.StructBlock):

    links = blocks.ListBlock(
        Link()
    )

    class Meta:
        template = "common/popular_pages_block.html"
        icon = "image"
        label = "Pages"
        help_text = "A set of pages"


class PagesTabBlock(blocks.StructBlock):
    name = blocks.CharBlock(
        max_length=50,
        help_text="The name of the tab"
    )

    page_blocks = blocks.StreamBlock([
        ("pages", PagesBlock()),
    ])

    class Meta:
        template = "common/pages_tab_block.html"
        icon = "image"
        label = "Page Tab"
        help_text = "A set of pages"


class PagesTabsBlock(blocks.StructBlock):
    tab_blocks = blocks.StreamBlock([
        ("tabs", PagesTabBlock()),
    ])

    class Meta:
        template = "common/pages_tabs_block.html"
        icon = "image"
        label = "Tabs"
        help_text = "A set of tabs containing pages"


class CardsBlock(blocks.StructBlock):
    cards = blocks.ListBlock(
        Card()
    )

    class Meta:
        template = "common/cards_block.html"
        icon = "image"
        label = "Cards"
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
        template = "common/image_and_text_block.html"
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
        ("text", blocks.RichTextBlock()),
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
        template = "common/subsubsection_block.html"
        label = "SubSubSection"
        help_text = "A subsubsection of the document"


class SubSectionBlock(GenericSectionBlock):  

    subcontent = blocks.StreamBlock(
        GenericSectionBlock.common_sections + [("subsubsection", SubSubSectionBlock())],
        required=False,
        help_text="The subsection's content"
    )

    class Meta:
        template = "common/subsection_block.html"
        label = "SubSection"
        help_text = "A subsubsection of the document"


class SectionBlock(GenericSectionBlock):

    subcontent = blocks.StreamBlock(
            GenericSectionBlock.common_sections + [("subsection", SubSectionBlock())],
            required=False,
            help_text="The section's content"
        )
    
    class Meta:
        template = "common/section_block.html"
        label = "Section"
        help_text = "A section of the document"


class UpdateBlock(blocks.StructBlock):
    title = blocks.CharBlock(
        max_length=150,
        help_text="The title of the update",
    )

    icon = blocks.CharBlock(
        max_length=50,
        help_text="The icon associated with this announcement",
        default="fa-regular fa-bell"
    )

    date = blocks.DateBlock(
        help_text="The date of this announcement"
    )

    text = blocks.RichTextBlock(
        help_text="A description of the update"
    )


class UpdatesBlock(blocks.StructBlock):
    updates = blocks.ListBlock(
        UpdateBlock()
    )

    class Meta:
        template = "common/updates_block.html"
        label = "Updates"
        help_text = "A set of update cards"