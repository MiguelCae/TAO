# Generated by Django 3.1.2 on 2020-10-15 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='persona',
            fields=[
                ('documento', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('correo', models.EmailField(max_length=80)),
                ('ciudad', models.CharField(max_length=50, null=True)),
                ('direccon', models.CharField(max_length=50, null=True)),
                ('ocupacion', models.CharField(max_length=50)),
                ('rol', models.CharField(max_length=50)),
            ],
        ),
    ]
