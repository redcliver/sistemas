# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-11 16:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lavajato_agenda', '0013_agenda_pagas_parcelas'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcela',
            name='data_pagamento',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
