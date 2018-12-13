# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-12 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chica_controle', '0006_auto_20181212_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='reg_ponto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(choices=[(b'1', b'Aberto'), (b'2', b'Confirmado')], max_length=1)),
                ('operacao', models.CharField(choices=[(b'1', b'Entrada'), (b'2', b'Saida')], max_length=1)),
                ('funcionario', models.CharField(max_length=200)),
                ('data_confirmacao', models.DateTimeField(blank=True, null=True)),
                ('data_cadastro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='ponto',
        ),
    ]
