# Generated by Django 3.0.6 on 2020-06-27 22:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0007_auto_20200627_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presupuesto',
            name='creado',
            field=models.DateTimeField(auto_created=datetime.datetime(2020, 6, 27, 22, 48, 54, 956534)),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='creado',
            field=models.DateTimeField(auto_created=datetime.datetime(2020, 6, 27, 22, 48, 54, 958147)),
        ),
    ]