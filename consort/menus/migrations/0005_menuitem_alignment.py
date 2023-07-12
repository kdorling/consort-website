# Generated by Django 4.2.1 on 2023-07-12 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0004_alter_menuitem_page_alter_submenuitem_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='alignment',
            field=models.IntegerField(choices=[(0, 'Left'), (1, 'Center'), (2, 'Right')], default=0),
            preserve_default=False,
        ),
    ]
