# Generated by Django 3.1.2 on 2020-11-10 15:36

from django.db import migrations, models
import django.db.models.deletion


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
                ('device_last_updated', models.DateTimeField(verbose_name='device last updated')),
                ('uptime', models.IntegerField(default=0)),
                ('boot_version_number', models.CharField(default='', max_length=20)),
                ('os_version_number', models.CharField(default='', max_length=20)),
                ('assets_page_url', models.CharField(default='', max_length=200)),
                ('serial', models.CharField(max_length=24)),
                ('ethernet_ip', models.CharField(max_length=20)),
                ('model', models.CharField(default='', max_length=10)),
                ('mac', models.CharField(default='', max_length=20)),
                ('video_mode', models.CharField(default='', max_length=20)),
                ('company', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Firmware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firmware_name', models.CharField(default='', max_length=20)),
                ('firmware_url', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Snapshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snapshot_datetime', models.DateTimeField(verbose_name='snapshot date')),
                ('snapshot_url', models.CharField(default='', max_length=200)),
                ('snapshot_path', models.CharField(default='', max_length=200)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bsa.device')),
            ],
        ),
    ]