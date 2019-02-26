# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-15 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lavajato_agenda', '0023_auto_20190207_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='estado',
            field=models.CharField(choices=[('1', 'Aberto'), ('2', 'Desmarcado'), ('3', 'Pago')], max_length=1),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='tipo',
            field=models.CharField(choices=[('1', 'Dinheiro'), ('2', 'Cartao Debito'), ('3', 'Cartao Credito'), ('4', 'Cartao Debito ELO'), ('5', 'Cartao Credito ELO')], max_length=1),
        ),
    ]