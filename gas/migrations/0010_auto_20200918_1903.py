# Generated by Django 3.1 on 2020-09-18 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gas', '0009_auto_20200918_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_number',
            field=models.CharField(blank=True, default='ZnZANbacCs', editable=False, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='connection',
            name='connection_number',
            field=models.CharField(blank=True, default='o7nhGOI6eK', editable=False, max_length=10, unique=True),
        ),
    ]
