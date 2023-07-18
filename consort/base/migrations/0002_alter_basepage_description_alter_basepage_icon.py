# Generated by Django 4.2.1 on 2023-07-12 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basepage',
            name='description',
            field=models.CharField(blank=True, default='', help_text="The page's description. Used in the menu and on cards", max_length=50),
        ),
        migrations.AlterField(
            model_name='basepage',
            name='icon',
            field=models.CharField(blank=True, default='', help_text="The page's icon", max_length=25),
        ),
    ]