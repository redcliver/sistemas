# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-19 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lavajato_contas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conta',
            name='data_pagamento',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
