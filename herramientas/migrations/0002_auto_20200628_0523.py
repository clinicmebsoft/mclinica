# Generated by Django 3.0.6 on 2020-06-28 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herramientas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codigo_postal',
            name='d_asenta',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='codigo_postal',
            name='d_tipo_asenta',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='codigo_postal',
            name='d_zona',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
