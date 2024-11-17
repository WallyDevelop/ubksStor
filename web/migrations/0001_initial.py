# Generated by Django 5.1.2 on 2024-11-05 20:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=12)),
                ('correo', models.EmailField(max_length=100)),
                ('contraseña', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField(null=True)),
                ('precio', models.IntegerField()),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('imagen', models.ImageField(upload_to='productos')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=9)),
                ('estado', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.cliente')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='web.producto')),
            ],
        ),
    ]
