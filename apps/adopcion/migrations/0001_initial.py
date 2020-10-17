# Generated by Django 3.1.2 on 2020-10-15 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestion_mascotas', '0001_initial'),
        ('control_usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='perfil_adoptar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto_adopcion', models.CharField(max_length=2500)),
                ('descripcion_adopcion', models.CharField(max_length=280)),
                ('mascota', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gestion_mascotas.mascota')),
            ],
        ),
        migrations.CreateModel(
            name='perfil_adoptante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('circulo_familiar', models.IntegerField()),
                ('experiencia_mascotas', models.IntegerField()),
                ('persona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='control_usuarios.persona')),
            ],
        ),
    ]