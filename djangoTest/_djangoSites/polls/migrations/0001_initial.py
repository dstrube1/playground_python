# Generated by Django 3.1.2 on 2020-10-27 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=20)),
                ('device_datetime', models.DateTimeField(verbose_name='device datetime')),
                ('device_datetime_text', models.CharField(max_length=200)),
                ('uptime', models.IntegerField(default=0)),
                ('boot_version_number', models.CharField(max_length=20)),
                ('os_version_number', models.CharField(max_length=20)),
                ('assets_page', models.CharField(max_length=200)),
                ('serial', models.CharField(max_length=24)),
                ('ethernet_ip', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=10)),
                ('mac', models.CharField(max_length=20)),
                ('video_mode', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Firmware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firmware_name', models.CharField(max_length=20)),
                ('firmware_page', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Snapshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=20)),
                ('snapshot_datetime', models.DateTimeField(verbose_name='date published')),
                ('snapshot_page', models.CharField(max_length=200)),
            ],
        ),
    ]
