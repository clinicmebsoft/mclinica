# Generated by Django 3.0.6 on 2020-06-26 23:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarios', '0004_auto_20200626_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulos',
            name='costo',
            field=models.FloatField(max_length=14),
        ),
        migrations.AlterField(
            model_name='articulos',
            name='creado',
            field=models.DateTimeField(auto_created=datetime.datetime(2020, 6, 26, 23, 32, 44, 364961)),
        ),
        migrations.AlterField(
            model_name='articulos',
            name='precioventa',
            field=models.FloatField(max_length=14),
        ),
        migrations.AlterField(
            model_name='impuestos',
            name='porcentaje',
            field=models.FloatField(blank=True, max_length=4, null=True),
        ),
    ]