# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-30 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Actividad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudadano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curp', models.CharField(max_length=20)),
                ('userName', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('monedas', models.IntegerField()),
            ],
        ),
    ]