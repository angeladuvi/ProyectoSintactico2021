# Generated by Django 3.2.8 on 2021-10-26 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
        migrations.CreateModel(
            name='tessiu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(verbose_name='temperatura')),
                ('color', models.FloatField()),
                ('inflamation', models.FloatField(verbose_name='inflamacion')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.paciente')),
            ],
            options={
                'verbose_name': 'tejido',
                'verbose_name_plural': 'tejidos',
            },
        ),
    ]
