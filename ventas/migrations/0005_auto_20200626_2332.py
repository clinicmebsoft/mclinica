# Generated by Django 3.0.6 on 2020-06-26 23:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0004_auto_20200626_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presupuesto',
            name='creado',
            field=models.DateTimeField(auto_created=datetime.datetime(2020, 6, 26, 23, 32, 44, 367166)),
        ),
        migrations.AlterField(
            model_name='ventas',
            name='creado',
            field=models.DateTimeField(auto_created=datetime.datetime(2020, 6, 26, 23, 32, 44, 368539)),
        ),
    ]