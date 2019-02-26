# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-15 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lavajato_estoque', '0002_auto_20190212_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lote',
            name='quantidade',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='produto',
            name='lucro',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='quantidade',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='produto',
            name='quantidade_minima',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='retiradas',
            name='quantidade',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='retiradas',
            name='uso',
            field=models.CharField(choices=[('1', 'Proprio'), ('2', 'Venda')], default=1, max_length=1),
        ),
    ]