# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-11 20:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lavajato_agenda', '0015_pagamento_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcela',
            name='numero_parcela',
            field=models.IntegerField(default=1),
        ),
    ]