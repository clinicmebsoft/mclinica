# Generated by Django 3.1.2 on 2021-01-06 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Codigo_postal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_codigo', models.CharField(blank=True, max_length=8, null=True)),
                ('d_asenta', models.CharField(blank=True, max_length=100, null=True)),
                ('d_tipo_asenta', models.CharField(blank=True, max_length=100, null=True)),
                ('d_mnpio', models.CharField(blank=True, max_length=80, null=True)),
                ('d_estado', models.CharField(blank=True, max_length=50, null=True)),
                ('d_ciudad', models.CharField(blank=True, max_length=50, null=True)),
                ('d_cp', models.CharField(blank=True, max_length=8, null=True)),
                ('c_estado', models.CharField(blank=True, max_length=8, null=True)),
                ('c_oficina', models.CharField(blank=True, max_length=8, null=True)),
                ('c_cp', models.CharField(blank=True, max_length=8, null=True)),
                ('c_tipo_asenta', models.CharField(blank=True, max_length=8, null=True)),
                ('c_mnpio', models.CharField(blank=True, max_length=8, null=True)),
                ('id_asenta_cpcons', models.CharField(blank=True, max_length=8, null=True)),
                ('d_zona', models.CharField(blank=True, max_length=100, null=True)),
                ('c_cve_ciudad', models.CharField(blank=True, max_length=8, null=True)),
            ],
            options={
                'ordering': ['d_codigo'],
            },
        ),
    ]
