# Generated by Django 3.1.7 on 2021-04-27 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tagging', '0002_auto_20210427_0550'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taggingresource',
            old_name='specific_topic',
            new_name='specific_topics',
        ),
    ]
