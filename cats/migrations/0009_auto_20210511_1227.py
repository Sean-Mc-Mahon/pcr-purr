# Generated by Django 3.1.7 on 2021-05-11 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0008_cat_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='age',
            field=models.CharField(help_text='Age when rescued', max_length=254),
        ),
    ]
