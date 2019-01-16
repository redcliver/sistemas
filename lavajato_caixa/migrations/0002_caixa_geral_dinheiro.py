# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-14 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lavajato_caixa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='caixa_geral',
            name='dinheiro',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]