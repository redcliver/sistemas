# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-15 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_cliente', '0011_auto_20190108_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='convenio',
            field=models.CharField(choices=[('1', 'ISS'), ('2', 'Estado MS'), ('3', 'SIAPE'), ('4', 'EXERCITO')], max_length=1),
        ),
    ]
