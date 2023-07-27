from wagtail import blocks
from wagtail.admin import widgets
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.blocks import SnippetChooserBlock

from base.models import BasePage
from profiles.models import Profile


class TitleBlock(blocks.StructBlock):
    text = blocks.CharBlock(
        required=True,
        help_text="Text to display",
    )

    alignment = blocks.ChoiceBlock(
        choices=(
            ("text-left", "Title to the left"),
            ("text-center", "Title centered"),
            ("text-right", "Title to the right")
        ),
        default="text-left", 
        help_text="Title for a section of the page"
    )

    header = blocks.ChoiceBlock(
        choices=(
            ("h1", "Large title (h1)"),
            ("h2", "Medium title (h2)"),
            ("h3", "Small title (h3)"),
        ),
        default="h1", 
        help_text="Header size"
    )

    class Meta:
        template = "flex/title_block.html"
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
        template = "flex/buttons_block.html"
        icon = "image"
        label = "Links"
        help_text = "A set of buttons on the page"


class PagesBlock(blocks.StructBlock):

    links = blocks.ListBlock(
        Link()
    )

    class Meta:
        template = "flex/pages_block.html"
        icon = "image"
        label = "Pages"
        help_text = "A set of pages"


class PopularPagesBlock(blocks.StructBlock):

    links = blocks.ListBlock(
        Link()
    )

    class Meta:
        template = "flex/popular_pages_block.html"
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
        template = "flex/pages_tab_block.html"
        icon = "image"
        label = "Page Tab"
        help_text = "A set of pages"


class PagesTabsBlock(blocks.StructBlock):
    tab_blocks = blocks.StreamBlock([
        ("tabs", PagesTabBlock()),
    ])

    class Meta:
        template = "flex/pages_tabs_block.html"
        icon = "image"
        label = "Tabs"
        help_text = "A set of tabs containing pages"


class CardsBlock(blocks.StructBlock):
    cards = blocks.ListBlock(
        Card()
    )

    class Meta:
        template = "flex/cards_block.html"
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
        template = "flex/image_and_text_block.html"
        icon = "image"
        label = "Image & Text"


class ProfileBlock(blocks.StructBlock):
    profile = SnippetChooserBlock(Profile)


class ProfilesBlock(blocks.StructBlock):
    profiles = blocks.ListBlock(
        ProfileBlock()
    )

    class Meta:
        template = "flex/profiles_block.html"
        label = "Profiles"
        help_text = "A set of user profiles"


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
        template = "flex/updates_block.html"
        label = "Updates"
        help_text = "A set of update cards"


class GenericSectionValue(blocks.StructValue):
    def anchor(self):
        header = self.get("header")
        return f"{header.lower().replace(' ', '_')}"


class GenericSectionBlock(blocks.StructBlock):
    common_sections = [
        ("cards", CardsBlock()),
        ("image_and_text", ImageAndTextBlock()),
        ("text", blocks.RichTextBlock()),
        ("profiles", ProfilesBlock()),
        ("title", TitleBlock()),
        ("cards", CardsBlock()),
        ("page_cards_with_tabs", PagesTabsBlock()),
        ("page_menu", PopularPagesBlock()),
        ("updates", UpdatesBlock()),
    ]

    # header = blocks.CharBlock(
    #     required=True,
    #     help_text="The section's title",
    # )

    # content = blocks.RichTextBlock(
    #     required=True,
    #     help_text="The section's content",
    # )

    class Meta:
        icon = "edit"
        value_class = GenericSectionValue


class SubSubSectionBlock(GenericSectionBlock):
    
    body = blocks.StreamBlock(
        GenericSectionBlock.common_sections,
        required=False,
        help_text="The subsubsection's subcontent"
    )

    class Meta:
        template = "flex/subsubsection_block.html"
        label = "SubSubSection"
        help_text = "A subsubsection of the document"


class SubSectionBlock(GenericSectionBlock):  

    body = blocks.StreamBlock(
        GenericSectionBlock.common_sections + [("subsubsection", SubSubSectionBlock())],
        required=False,
        help_text="The subsection's content"
    )

    class Meta:
        template = "flex/subsection_block.html"
        label = "SubSection"
        help_text = "A subsubsection of the document"


class SectionBlock(GenericSectionBlock):

    body = blocks.StreamBlock(
            GenericSectionBlock.common_sections + [("subsection", SubSectionBlock())],
            required=False,
            help_text="The section's content"
        )
    
    class Meta:
        template = "flex/section_block.html"
        label = "Section"
        help_text = "A section of the document"


class SectionWithBackgroundBlock(GenericSectionBlock):

    body = blocks.StreamBlock(
            GenericSectionBlock.common_sections + [("subsection", SubSectionBlock())],
            required=False,
            help_text="The section's content"
        )
    
    background_color = blocks.ChoiceBlock(
        choices=[
            ("bg-white", "White"),
            ("bg-neutral-200", "Gray"),
            ("bg-orange-200", "Orange"),
        ], 
        default="white",
        help_text="The section's background color"
    )
    
    class Meta:
        template = "flex/section_block.html"
        label = "Section"
        help_text = "A section of the document"
