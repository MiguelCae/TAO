# Generated by Django 3.1.2 on 2020-10-17 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopcion', '0002_auto_20201016_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil_adoptar',
            name='descripcion_adopcion',
            field=models.TextField(max_length=280),
        ),
        migrations.AlterField(
            model_name='perfil_adoptar',
            name='foto_adopcion',
            field=models.CharField(max_length=250),
        ),
    ]