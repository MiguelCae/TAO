# Generated by Django 3.1.2 on 2020-10-15 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mascota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('especie', models.CharField(max_length=50, null=True)),
                ('raza', models.CharField(max_length=50, null=True)),
                ('tamaño', models.CharField(max_length=50, null=True)),
                ('sexo', models.CharField(max_length=10)),
                ('edad_aproximada', models.IntegerField()),
                ('fecha_rescate', models.DateField()),
                ('estado', models.CharField(max_length=50, null=True)),
                ('descripcion_mascota', models.CharField(max_length=50)),
                ('foto_mascota', models.CharField(max_length=250)),
            ],
        ),
    ]
