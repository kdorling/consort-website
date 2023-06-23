# Generated by Django 4.2.1 on 2023-06-23 01:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0083_workflowcontenttype'),
        ('base', '0001_initial'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='RedirectorPage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.basepage')),
                ('redirect_to', models.URLField(help_text='The URL to redirect to')),
            ],
            options={
                'verbose_name': 'Redirector',
            },
            bases=('base.basepage',),
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('basepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.basepage')),
                ('banner_title', models.CharField(blank=True, help_text='The banner title', max_length=50)),
                ('banner_subtitle', models.CharField(blank=True, help_text='Text under the banner title', max_length=150)),
                ('banner_button1_text', models.CharField(default='Why Move', help_text='Text for first button on the banner', max_length=50)),
                ('banner_button2_text', models.CharField(default='Open a Business', help_text='Text for second button on the banner', max_length=50)),
                ('banner_button3_text', models.CharField(default='Job Board', help_text='Text for third button on the banner', max_length=50)),
                ('information_title', models.CharField(default='Information', help_text='Information section title text', max_length=50)),
                ('residents_button_text', models.CharField(default='Residents', help_text='Text for the residents button', max_length=25)),
                ('residents_small_item1_text', models.CharField(default='', help_text='Text for first small residents item', max_length=25)),
                ('residents_small_item1_icon', models.CharField(default='', help_text='Icon for first small residents item', max_length=25)),
                ('residents_small_item2_text', models.CharField(default='', help_text='Text for second small residents item', max_length=25)),
                ('residents_small_item2_icon', models.CharField(default='', help_text='Icon for second small residents item', max_length=25)),
                ('residents_small_item3_text', models.CharField(default='', help_text='Text for third small residents item', max_length=25)),
                ('residents_small_item3_icon', models.CharField(default='', help_text='Icon for third small residents item', max_length=25)),
                ('residents_small_item4_text', models.CharField(default='', help_text='Text for fourth small residents item', max_length=25)),
                ('residents_small_item4_icon', models.CharField(default='', help_text='Icon for fourth small residents item', max_length=25)),
                ('residents_large_item1_text', models.CharField(default='', help_text='Text for first large residents item', max_length=25)),
                ('residents_large_item1_subtext', models.CharField(default='', help_text='Subtext for first large residents item', max_length=25)),
                ('residents_large_item2_text', models.CharField(default='', help_text='Text for second large residents item', max_length=25)),
                ('residents_large_item2_subtext', models.CharField(default='', help_text='Subtext for second large residents item', max_length=25)),
                ('businesses_button_text', models.CharField(default='Businesses', help_text='Text for the businesses button', max_length=25)),
                ('businesses_small_item1_text', models.CharField(default='', help_text='Text for first small businesses item', max_length=25)),
                ('businesses_small_item1_icon', models.CharField(default='', help_text='Icon for first small businesses item', max_length=25)),
                ('businesses_small_item2_text', models.CharField(default='', help_text='Text for second small businesses item', max_length=25)),
                ('businesses_small_item2_icon', models.CharField(default='', help_text='Icon for second small businesses item', max_length=25)),
                ('businesses_small_item3_text', models.CharField(default='', help_text='Text for third small businesses item', max_length=25)),
                ('businesses_small_item3_icon', models.CharField(default='', help_text='Icon for third small businesses item', max_length=25)),
                ('businesses_small_item4_text', models.CharField(default='', help_text='Text for fourth small businesses item', max_length=25)),
                ('businesses_small_item4_icon', models.CharField(default='', help_text='Icon for fourth small businesses item', max_length=25)),
                ('businesses_large_item1_text', models.CharField(default='', help_text='Text for first large businesses item', max_length=25)),
                ('businesses_large_item1_subtext', models.CharField(default='', help_text='Subtext for first large businesses item', max_length=25)),
                ('businesses_large_item2_text', models.CharField(default='', help_text='Text for second large businesses item', max_length=25)),
                ('businesses_large_item2_subtext', models.CharField(default='', help_text='Subtext for second large businesses item', max_length=25)),
                ('visitors_button_text', models.CharField(default='Visitors', help_text='Text for the visitors button', max_length=25)),
                ('visitors_small_item1_text', models.CharField(default='', help_text='Text for first small visitors item', max_length=25)),
                ('visitors_small_item1_icon', models.CharField(default='', help_text='Icon for first small visitors item', max_length=25)),
                ('visitors_small_item2_text', models.CharField(default='', help_text='Text for second small visitors item', max_length=25)),
                ('visitors_small_item2_icon', models.CharField(default='', help_text='Icon for second small visitors item', max_length=25)),
                ('visitors_small_item3_text', models.CharField(default='', help_text='Text for third small visitors item', max_length=25)),
                ('visitors_small_item3_icon', models.CharField(default='', help_text='Icon for third small visitors item', max_length=25)),
                ('visitors_small_item4_text', models.CharField(default='', help_text='Text for fourth small visitors item', max_length=25)),
                ('visitors_small_item4_icon', models.CharField(default='', help_text='Icon for fourth small visitors item', max_length=25)),
                ('visitors_large_item1_text', models.CharField(default='', help_text='Text for first large visitors item', max_length=25)),
                ('visitors_large_item1_subtext', models.CharField(default='', help_text='Subtext for first large visitors item', max_length=25)),
                ('visitors_large_item2_text', models.CharField(default='', help_text='Text for second large visitors item', max_length=25)),
                ('visitors_large_item2_subtext', models.CharField(default='', help_text='Subtext for second large visitors item', max_length=25)),
                ('popular_pages_title', models.CharField(default='Popular Pages', help_text='Popular pages section title text', max_length=50)),
                ('popular_pages_item1_text', models.CharField(default='', help_text='Text for first popular page', max_length=25)),
                ('popular_pages_item1_icon', models.CharField(default='', help_text='Icon for first popular page', max_length=25)),
                ('popular_pages_item2_text', models.CharField(default='', help_text='Text for second popular page', max_length=25)),
                ('popular_pages_item2_icon', models.CharField(default='', help_text='Icon for second popular page', max_length=25)),
                ('popular_pages_item3_text', models.CharField(default='', help_text='Text for third popular page', max_length=25)),
                ('popular_pages_item3_icon', models.CharField(default='', help_text='Icon for third popular page', max_length=25)),
                ('popular_pages_item4_text', models.CharField(default='', help_text='Text for fourth popular page', max_length=25)),
                ('popular_pages_item4_icon', models.CharField(default='', help_text='Icon for fourth popular page', max_length=25)),
                ('banner_background_image', models.ForeignKey(help_text='The banner background image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('banner_button1_link', models.ForeignKey(help_text='Link for first button on the banner', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('banner_button2_link', models.ForeignKey(help_text='Link for second button on the banner', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('banner_button3_link', models.ForeignKey(help_text='Third button on the banner', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('businesses_large_item1_image', models.ForeignKey(help_text='Image for first large businesses item', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('businesses_large_item1_link', models.ForeignKey(help_text='Link for first large businesses item', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('businesses_large_item2_image', models.ForeignKey(help_text='Image for second large businesses item', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('businesses_large_item2_link', models.ForeignKey(help_text='Link for second large businesses item', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('businesses_small_item1_link', models.ForeignKey(help_text='Link for first small businesses item', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('businesses_small_item2_link', models.ForeignKey(help_text='Link for second small businesses item', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('businesses_small_item3_link', models.ForeignKey(help_text='Link for third small businesses item', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('businesses_small_item4_link', models.ForeignKey(help_text='Link for fourth small businesses item', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('popular_pages_item1_link', models.ForeignKey(help_text='Link for first popular page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('popular_pages_item2_link', models.ForeignKey(help_text='Link for second popular page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('popular_pages_item3_link', models.ForeignKey(help_text='Link for third popular page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('popular_pages_item4_link', models.ForeignKey(help_text='Link for fourth popular page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('residents_large_item1_image', models.ForeignKey(help_text='Image for first large residents item', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('residents_large_item1_link', models.ForeignKey(help_text='Link for first large residents item', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('residents_large_item2_image', models.ForeignKey(help_text='Image for second large residents item', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('residents_large_item2_link', models.ForeignKey(help_text='Link for second large residents item', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('residents_small_item1_link', models.ForeignKey(help_text='Link for first small residents item', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('residents_small_item2_link', models.ForeignKey(help_text='Link for second small residents item', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('residents_small_item3_link', models.ForeignKey(help_text='Link for third small residents item', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('residents_small_item4_link', models.ForeignKey(help_text='Link for fourth small residents item', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('visitors_large_item1_image', models.ForeignKey(help_text='Image for first large visitors item', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('visitors_large_item1_link', models.ForeignKey(help_text='Link for first large visitors item', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('visitors_large_item2_image', models.ForeignKey(help_text='Image for second large visitors item', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('visitors_large_item2_link', models.ForeignKey(help_text='Link for second large visitors item', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('visitors_small_item1_link', models.ForeignKey(help_text='Link for first small visitors item', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('visitors_small_item2_link', models.ForeignKey(help_text='Link for second small visitors item', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('visitors_small_item3_link', models.ForeignKey(help_text='Link for third small visitors item', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
                ('visitors_small_item4_link', models.ForeignKey(help_text='Link for fourth small visitors item', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('base.basepage',),
        ),
    ]
