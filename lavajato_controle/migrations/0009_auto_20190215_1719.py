# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-15 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lavajato_controle', '0008_auto_20190206_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conta_empresa',
            name='operacao',
            field=models.CharField(choices=[('1', 'Entrada'), ('2', 'Saida')], max_length=1),
        ),
        migrations.AlterField(
            model_name='taxa',
            name='tipo',
            field=models.CharField(choices=[('1', 'Credito a Vista'), ('2', 'Credito a Prazo'), ('3', 'Debito'), ('4', 'Debito Elo'), ('5', 'Credito Elo'), ('6', 'Boleto')], max_length=1),
        ),
    ]
