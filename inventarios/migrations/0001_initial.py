# Generated by Django 3.0.6 on 2020-06-20 02:21

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField(max_length=60)),
                ('estatus', models.CharField(max_length=2)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Fabricantes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fabricante', models.TextField(max_length=60)),
                ('estatus', models.CharField(max_length=2)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Impuestos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('impuesto', models.TextField(max_length=30)),
                ('pocertanje', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('estatus', models.CharField(max_length=2)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Marcas',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('marca', models.TextField(max_length=60)),
                ('estatus', models.CharField(max_length=2)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('provedoor', models.TextField(max_length=30)),
                ('estatus', models.CharField(max_length=2)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Unidades',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('unidad', models.TextField(max_length=60)),
                ('estatus', models.CharField(max_length=2)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('creado', models.DateTimeField(auto_created=datetime.datetime(2020, 6, 20, 2, 21, 14, 583081))),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=1)),
                ('codigo', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=120)),
                ('codigobarras', models.CharField(max_length=20)),
                ('precioventa', models.DecimalField(decimal_places=2, max_digits=9, max_length=14)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=9, max_length=14)),
                ('stock_min', models.IntegerField(max_length=9)),
                ('stock_max', models.IntegerField(max_length=9)),
                ('reorden', models.IntegerField(max_length=6)),
                ('cantidad', models.IntegerField(max_length=6)),
                ('actualizado', models.DateTimeField(auto_now_add=True)),
                ('estatus', models.CharField(max_length=2)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventarios.Categorias')),
                ('id_fabricantes', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventarios.Fabricantes')),
                ('id_impuestos', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventarios.Impuestos')),
                ('id_marcas', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventarios.Marcas')),
                ('id_proveedores', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventarios.Proveedores')),
                ('id_unidades', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventarios.Unidades')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
