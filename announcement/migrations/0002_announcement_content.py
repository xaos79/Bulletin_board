# Generated by Django 3.2.9 on 2021-11-21 11:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='content',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
