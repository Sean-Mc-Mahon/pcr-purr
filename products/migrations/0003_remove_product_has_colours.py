# Generated by Django 3.1.7 on 2021-05-13 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210414_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='has_colours',
        ),
    ]
