# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-11 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lavajato_agenda', '0014_parcela_data_pagamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagamento',
            name='descricao',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
