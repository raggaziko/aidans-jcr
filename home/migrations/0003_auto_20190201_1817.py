# Generated by Django 2.1.5 on 2019-02-01 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailmenus', '0022_auto_20170913_2125'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('home', '0002_auto_20190115_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serveryday',
            name='page',
        ),
        migrations.RemoveField(
            model_name='serverypage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='ServeryDay',
        ),
        migrations.DeleteModel(
            name='ServeryPage',
        ),
    ]