# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-20 15:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lavajato_agenda', '0027_auto_20190219_0414'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='data_pagamento',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
