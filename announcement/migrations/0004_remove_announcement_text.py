# Generated by Django 3.2.9 on 2021-11-21 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0003_alter_announcement_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='text',
        ),
    ]