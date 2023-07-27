# Generated by Django 4.2.3 on 2023-07-26 19:54

from django.db import migrations, models
import django.db.models.deletion
import flex.blocks
import profiles.models
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.basepage')),
                ('banner_title', models.CharField(help_text="The banner's title", max_length=50)),
                ('banner_title_emphasis', models.CharField(help_text="The emphasized part of the banner's title", max_length=50)),
                ('banner_text', wagtail.fields.RichTextField(help_text='Text under the banner')),
                ('banner_buttons', wagtail.fields.StreamField([('buttons', wagtail.blocks.StructBlock([('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('link_text', wagtail.blocks.CharBlock(default='More Details', max_length=50)), ('page', flex.blocks.BasePageChooserBlock(required=False))]))), ('button_styles', wagtail.blocks.CharBlock(help_text='Tailwind classes to style the buttons', max_length=150, required=False))]))], use_json_field=True)),
                ('body', wagtail.fields.StreamField([('section', wagtail.blocks.StructBlock([('body', wagtail.blocks.StreamBlock([('cards', wagtail.blocks.StructBlock([('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Bold title text for this card. Max length of 100 characters.', max_length=100)), ('text', wagtail.blocks.TextBlock(help_text='Optional text for this card. Max length is 255 characters.', max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image will be automatically cropped to 570px x 370px')), ('link', wagtail.blocks.StructBlock([('link_text', wagtail.blocks.CharBlock(default='More Details', max_length=50)), ('page', flex.blocks.BasePageChooserBlock(required=False))], help_text='Enter a link or select a page'))])))])), ('image_and_text', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image automatically cropped to 786px by 552px', required=True)), ('image_alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Image to the left'), ('right', 'Image to the right')], help_text='Image on one side of the screen, with text on the other')), ('title', wagtail.blocks.CharBlock(help_text='Max length of 60 characters.', max_length=60)), ('text', wagtail.blocks.CharBlock(max_length=140, required=False)), ('link', wagtail.blocks.StructBlock([('link_text', wagtail.blocks.CharBlock(default='More Details', max_length=50)), ('page', flex.blocks.BasePageChooserBlock(required=False))]))])), ('text', wagtail.blocks.RichTextBlock()), ('profiles', wagtail.blocks.StructBlock([('profiles', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('profile', wagtail.snippets.blocks.SnippetChooserBlock(profiles.models.Profile))])))])), ('title', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(help_text='Text to display', required=True)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('text-left', 'Title to the left'), ('text-center', 'Title centered'), ('text-right', 'Title to the right')], help_text='Title for a section of the page')), ('header', wagtail.blocks.ChoiceBlock(choices=[('h1', 'Large title (h1)'), ('h2', 'Medium title (h2)'), ('h3', 'Small title (h3)')], help_text='Header size'))])), ('page_cards_with_tabs', wagtail.blocks.StructBlock([('tab_blocks', wagtail.blocks.StreamBlock([('tabs', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(help_text='The name of the tab', max_length=50)), ('page_blocks', wagtail.blocks.StreamBlock([('pages', wagtail.blocks.StructBlock([('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('link_text', wagtail.blocks.CharBlock(default='More Details', max_length=50)), ('page', flex.blocks.BasePageChooserBlock(required=False))])))]))]))]))]))])), ('page_menu', wagtail.blocks.StructBlock([('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('link_text', wagtail.blocks.CharBlock(default='More Details', max_length=50)), ('page', flex.blocks.BasePageChooserBlock(required=False))])))])), ('updates', wagtail.blocks.StructBlock([('updates', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='The title of the update', max_length=150)), ('icon', wagtail.blocks.CharBlock(default='fa-regular fa-bell', help_text='The icon associated with this announcement', max_length=50)), ('date', wagtail.blocks.DateBlock(help_text='The date of this announcement')), ('text', wagtail.blocks.RichTextBlock(help_text='A description of the update'))])))])), ('subsection', wagtail.blocks.StructBlock([('body', wagtail.blocks.StreamBlock([('cards', wagtail.blocks.StructBlock([('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Bold title text for this card. Max length of 100 characters.', max_length=100)), ('text', wagtail.blocks.TextBlock(help_text='Optional text for this card. Max length is 255 characters.', max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image will be automatically cropped to 570px x 370px')), ('link', wagtail.blocks.StructBlock([('link_text', wagtail.blocks.CharBlock(default='More Details', max_length=50)), ('page', flex.blocks.BasePageChooserBlock(required=False))], help_text='Enter a link or select a page'))])))])), ('image_and_text', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image automatically cropped to 786px by 552px', required=True)), ('image_alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Image to the left'), ('right', 'Image to the right')], help_text='Image on one side of the screen, with text on the other')), ('title', wagtail.blocks.CharBlock(help_text='Max length of 60 characters.', max_length=60)), ('text', wagtail.blocks.CharBlock(max_length=140, required=False)), ('link', wagtail.blocks.StructBlock([('link_text', wagtail.blocks.CharBlock(default='More Details', max_length=50)), ('page', flex.blocks.BasePageChooserBlock(required=False))]))])), ('text', wagtail.blocks.RichTextBlock()), ('profiles', wagtail.blocks.StructBlock([('profiles', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('profile', wagtail.snippets.blocks.SnippetChooserBlock(profiles.models.Profile))])))])), ('title', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(help_text='Text to display', required=True)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('text-left', 'Title to the left'), ('text-center', 'Title centered'), ('text-right', 'Title to the right')], help_text='Title for a section of the page')), ('header', wagtail.blocks.ChoiceBlock(choices=[('h1', 'Large title (h1)'), ('h2', 'Medium title (h2)'), ('h3', 'Small title (h3)')], help_text='Header size'))])), ('page_cards_with_tabs', wagtail.blocks.StructBlock([('tab_blocks', wagtail.blocks.StreamBlock([('tabs', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(help_text='The name of the tab', max_length=50)), ('page_blocks', wagtail.blocks.StreamBlock([('pages', wagtail.blocks.StructBlock([('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('link_text', wagtail.blocks.CharBlock(default='More Details', max_length=50)), ('page', flex.blocks.BasePageChooserBlock(required=False))])))]))]))]))]))])), ('page_menu', wagtail.blocks.StructBlock([('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('link_text', wagtail.blocks.CharBlock(default='More Details', max_length=50)), ('page', flex.blocks.BasePageChooserBlock(required=False))])))])), ('updates', wagtail.blocks.StructBlock([('updates', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='The title of the update', max_length=150)), ('icon', wagtail.blocks.CharBlock(default='fa-regular fa-bell', help_text='The icon associated with this announcement', max_length=50)), ('date', wagtail.blocks.DateBlock(help_text='The date of this announcement')), ('text', wagtail.blocks.RichTextBlock(help_text='A description of the update'))])))])), ('subsubsection', wagtail.blocks.StructBlock([('body', wagtail.blocks.StreamBlock([('cards', wagtail.blocks.StructBlock([('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Bold title text for this card. Max length of 100 characters.', max_length=100)), ('text', wagtail.blocks.TextBlock(help_text='Optional text for this card. Max length is 255 characters.', max_length=255, required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image will be automatically cropped to 570px x 370px')), ('link', wagtail.blocks.StructBlock([('link_text', wagtail.blocks.CharBlock(default='More Details', max_length=50)), ('page', flex.blocks.BasePageChooserBlock(required=False))], help_text='Enter a link or select a page'))])))])), ('image_and_text', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Image automatically cropped to 786px by 552px', required=True)), ('image_alignment', wagtail.blocks.ChoiceBlock(choices=[('left', 'Image to the left'), ('right', 'Image to the right')], help_text='Image on one side of the screen, with text on the other')), ('title', wagtail.blocks.CharBlock(help_text='Max length of 60 characters.', max_length=60)), ('text', wagtail.blocks.CharBlock(max_length=140, required=False)), ('link', wagtail.blocks.StructBlock([('link_text', wagtail.blocks.CharBlock(default='More Details', max_length=50)), ('page', flex.blocks.BasePageChooserBlock(required=False))]))])), ('text', wagtail.blocks.RichTextBlock()), ('profiles', wagtail.blocks.StructBlock([('profiles', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('profile', wagtail.snippets.blocks.SnippetChooserBlock(profiles.models.Profile))])))])), ('title', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(help_text='Text to display', required=True)), ('alignment', wagtail.blocks.ChoiceBlock(choices=[('text-left', 'Title to the left'), ('text-center', 'Title centered'), ('text-right', 'Title to the right')], help_text='Title for a section of the page')), ('header', wagtail.blocks.ChoiceBlock(choices=[('h1', 'Large title (h1)'), ('h2', 'Medium title (h2)'), ('h3', 'Small title (h3)')], help_text='Header size'))])), ('page_cards_with_tabs', wagtail.blocks.StructBlock([('tab_blocks', wagtail.blocks.StreamBlock([('tabs', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock(help_text='The name of the tab', max_length=50)), ('page_blocks', wagtail.blocks.StreamBlock([('pages', wagtail.blocks.StructBlock([('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('link_text', wagtail.blocks.CharBlock(default='More Details', max_length=50)), ('page', flex.blocks.BasePageChooserBlock(required=False))])))]))]))]))]))])), ('page_menu', wagtail.blocks.StructBlock([('links', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('link_text', wagtail.blocks.CharBlock(default='More Details', max_length=50)), ('page', flex.blocks.BasePageChooserBlock(required=False))])))])), ('updates', wagtail.blocks.StructBlock([('updates', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='The title of the update', max_length=150)), ('icon', wagtail.blocks.CharBlock(default='fa-regular fa-bell', help_text='The icon associated with this announcement', max_length=50)), ('date', wagtail.blocks.DateBlock(help_text='The date of this announcement')), ('text', wagtail.blocks.RichTextBlock(help_text='A description of the update'))])))]))], help_text="The subsubsection's subcontent", required=False))]))], help_text="The subsection's content", required=False))]))], help_text="The section's content", required=False)), ('background_color', wagtail.blocks.ChoiceBlock(choices=[('bg-white', 'White'), ('bg-neutral-200', 'Gray'), ('bg-orange-200', 'Orange')], help_text="The section's background color"))]))], use_json_field=True)),
                ('banner_background_image', models.ForeignKey(help_text='The banner background image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('base.basepage',),
        ),
    ]
