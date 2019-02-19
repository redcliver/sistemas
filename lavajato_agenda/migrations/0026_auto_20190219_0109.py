# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-19 04:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lavajato_agenda', '0025_agenda_pag_parcial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagamento',
            name='tipo',
            field=models.CharField(choices=[('1', 'Dinheiro'), ('2', 'Cartao Debito'), ('3', 'Cartao Credito'), ('4', 'Cartao Debito ELO'), ('5', 'Cartao Credito ELO'), ('6', 'Boleto'), ('7', 'Transferencia')], max_length=1),
        ),
        migrations.AlterField(
            model_name='parcela',
            name='pag',
            field=models.CharField(choices=[('1', 'Dinheiro'), ('2', 'Cartao Debito'), ('3', 'Cartao Credito'), ('4', 'Cartao Debito ELO'), ('5', 'Cartao Credito ELO'), ('6', 'Boleto'), ('7', 'Transferencia')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]
