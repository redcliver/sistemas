# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-13 21:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chica_agenda', '0002_auto_20181204_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='pagamento',
            field=models.CharField(choices=[(b'1', b'Dinheiro'), (b'2', b'Cartao Debito'), (b'3', b'Cartao Credito'), (b'4', b'Aberto'), (b'5', b'Desmarcado')], max_length=1),
        ),
    ]
