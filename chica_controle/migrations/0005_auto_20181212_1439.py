# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-12 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chica_controle', '0004_auto_20181212_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ponto',
            name='modo',
            field=models.CharField(choices=[((b'1', b'Aberto'), (b'2', b'Confirmado'))], max_length=1),
        ),
    ]