# Generated by Django 4.2.7 on 2023-12-28 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_commentmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentmodel',
            old_name='board',
            new_name='post',
        ),
    ]
