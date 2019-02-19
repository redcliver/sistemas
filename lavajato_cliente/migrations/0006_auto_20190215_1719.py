# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-15 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lavajato_cliente', '0005_cliente_liberacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='liberacao',
            field=models.CharField(choices=[('1', 'Ok'), ('2', 'Bloqueado')], default=1, max_length=1),
        ),
    ]
