# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-19 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chica_controle', '0007_auto_20181212_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg_ponto',
            name='estado',
            field=models.CharField(choices=[('1', 'Aberto'), ('2', 'Confirmado')], max_length=1),
        ),
        migrations.AlterField(
            model_name='reg_ponto',
            name='operacao',
            field=models.CharField(choices=[('1', 'Entrada'), ('2', 'Saida')], max_length=1),
        ),
    ]