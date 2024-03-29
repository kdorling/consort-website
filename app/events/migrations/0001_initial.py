# Generated by Django 4.2.3 on 2023-08-01 02:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields
import wagtail.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('wagtaildocs', '0012_uploadeddocument'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailcore', '0083_workflowcontenttype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('live', models.BooleanField(default=True, editable=False, verbose_name='live')),
                ('has_unpublished_changes', models.BooleanField(default=False, editable=False, verbose_name='has unpublished changes')),
                ('first_published_at', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='first published at')),
                ('last_published_at', models.DateTimeField(editable=False, null=True, verbose_name='last published at')),
                ('go_live_at', models.DateTimeField(blank=True, null=True, verbose_name='go live date/time')),
                ('expire_at', models.DateTimeField(blank=True, null=True, verbose_name='expiry date/time')),
                ('expired', models.BooleanField(default=False, editable=False, verbose_name='expired')),
                ('locked', models.BooleanField(default=False, editable=False, verbose_name='locked')),
                ('locked_at', models.DateTimeField(editable=False, null=True, verbose_name='locked at')),
                ('name', models.CharField(help_text='The name of the event', max_length=255)),
                ('description', wagtail.fields.RichTextField(blank=True, help_text='The description of the event', null=True)),
                ('all_day', models.BooleanField(default=False, help_text='Does this event last all day?')),
                ('start_time', models.DateTimeField(help_text='The date and time when the event begins', null=True)),
                ('end_time', models.DateTimeField(help_text='The date and time when the event ends', null=True)),
                ('featured', models.BooleanField(default=False, help_text='Is this event featured? (Note: Recurring events cannot be featured.)')),
                ('frequency', models.CharField(blank=True, choices=[('DAILY', 'Daily'), ('WEEKLY', 'Weekly'), ('MONTHLY', 'Monthly'), ('YEARLY', 'Yearly')], default='WEEKLY', help_text='When does this event repeat?', max_length=8, null=True)),
                ('interval', models.IntegerField(blank=True, default=1, help_text='How often does this event occur?', null=True)),
                ('bymonth', models.IntegerField(blank=True, help_text='The month when this event occurs', null=True)),
                ('bymonthday', models.IntegerField(blank=True, help_text='The day of the month when this event occurs', null=True)),
                ('byyearday', models.IntegerField(blank=True, help_text='The day of the year when this event occurs', null=True)),
                ('byeaster', models.IntegerField(blank=True, help_text='The day of Easter', null=True)),
                ('byweekno', models.IntegerField(blank=True, help_text='The week of the year when this event occurs', null=True)),
                ('byweekday', models.IntegerField(blank=True, help_text='The day of the week when this event occurs', null=True)),
                ('document', models.ForeignKey(blank=True, help_text='A document associated with the event', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.document')),
                ('image', models.ForeignKey(blank=True, help_text='The image associated with the event', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('latest_revision', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='latest revision')),
                ('live_revision', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='live revision')),
                ('locked_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='locked_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='locked by')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
            bases=(wagtail.models.WorkflowMixin, models.Model),
        ),
    ]
