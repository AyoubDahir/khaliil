# Generated by Django 3.1 on 2020-10-05 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gas', '0018_gasreffiling_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'Booking', 'verbose_name_plural': '5.Booking'},
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('gas_reffiling', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gas.gasreffiling')),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': '4.Stock',
            },
        ),
    ]
