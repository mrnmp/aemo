# Generated by Django 3.1.2 on 2020-10-15 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nmi', models.CharField(max_length=100)),
                ('meter_serial_number', models.CharField(max_length=100)),
                ('reading', models.CharField(max_length=100)),
                ('reading_datetime', models.CharField(max_length=100)),
                ('file_name', models.CharField(max_length=100)),
            ],
        ),
    ]
