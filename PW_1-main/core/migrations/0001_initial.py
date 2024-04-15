# Generated by Django 2.2.28 on 2024-04-15 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PDF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('materia', models.CharField(max_length=100)),
                ('carrera', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=20)),
                ('objetivos', models.TextField(blank=True, null=True)),
                ('fundamentacion', models.TextField(blank=True, null=True)),
                ('contenido', models.TextField(blank=True, null=True)),
                ('metodologia', models.TextField(blank=True, null=True)),
                ('evaluacion', models.TextField(blank=True, null=True)),
                ('bibliografia', models.TextField()),
            ],
        ),
    ]
