# Generated by Django 3.1.2 on 2020-10-27 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_device_device_last_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='device_last_updated',
        ),
    ]
