# Generated by Django 3.1.7 on 2021-05-19 14:29

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_option', models.CharField(max_length=254)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Volunteering',
            },
        ),
        migrations.AlterModelOptions(
            name='volunteer',
            options={'verbose_name_plural': 'Volunteering'},
        ),
    ]
