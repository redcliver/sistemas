# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-08 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_cliente', '0010_auto_20190107_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='responsavel',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cliente_portabilidade',
            name='responsavel',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
