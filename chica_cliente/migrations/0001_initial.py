# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-08 15:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('data_nasc', models.DateTimeField(blank=True, null=True)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('celular', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('data_cadastro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
