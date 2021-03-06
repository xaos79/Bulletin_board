# Generated by Django 3.2.9 on 2021-11-26 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0004_remove_announcement_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='create',
            field=models.DateTimeField(auto_now_add=True, default='2021-11-26 20:21:23.231445'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='announcement',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='respond',
            name='create',
            field=models.DateTimeField(auto_now_add=True, default='2021-11-26 20:21:23.231445'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='respond',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='respond',
            name='text',
            field=models.TextField(verbose_name=''),
        ),
    ]
