# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-11 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lavajato_agenda', '0011_auto_20190111_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='total_parcelas',
            field=models.IntegerField(default=1),
        ),
    ]