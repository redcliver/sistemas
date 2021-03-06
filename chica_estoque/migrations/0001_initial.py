# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-20 14:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='produto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('valor_venda', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_compra', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade', models.IntegerField()),
                ('quantidade_minima', models.IntegerField()),
                ('lucro', models.IntegerField(blank=True, null=True)),
                ('data_cadastro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
