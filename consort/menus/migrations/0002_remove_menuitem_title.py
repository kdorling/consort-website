# Generated by Django 4.2.1 on 2023-07-11 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='title',
        ),
    ]
