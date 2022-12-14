# Generated by Django 3.1 on 2020-09-18 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gas', '0008_auto_20200918_0008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'Booking', 'verbose_name_plural': '3.Booking'},
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_number',
            field=models.CharField(blank=True, default='9201484289', editable=False, max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gas.staff'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='status',
            field=models.CharField(blank=True, choices=[('1', 'Confirmed'), ('2', 'On The Way'), ('3', 'Delivered')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='connection',
            name='connection_number',
            field=models.CharField(blank=True, default='9874457867', editable=False, max_length=10, unique=True),
        ),
    ]
