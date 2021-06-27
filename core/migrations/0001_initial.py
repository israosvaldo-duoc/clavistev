# Generated by Django 3.2.3 on 2021-06-27 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compania',
            fields=[
                ('idCompania', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Compañia')),
                ('nombreCompania', models.CharField(max_length=25, verbose_name='Nombre Compañia')),
            ],
        ),
        migrations.CreateModel(
            name='Celular',
            fields=[
                ('idCelular', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id Celular')),
                ('marca', models.CharField(max_length=30, verbose_name='Marca Celular')),
                ('modelo', models.CharField(max_length=30, verbose_name='Modelo Celular')),
                ('compania', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.compania')),
            ],
        ),
    ]
