# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-08 21:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lavajato_agenda', '0005_auto_20190108_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='pagamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(choices=[(b'1', b'Dinheiro'), (b'2', b'Cartao Debito'), (b'3', b'Cartao Credito')], max_length=1)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
