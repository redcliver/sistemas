# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-11 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lavajato_agenda', '0012_auto_20190111_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='pagas_parcelas',
            field=models.IntegerField(default=0),
        ),
    ]