# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-07 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('top_cliente', '0007_cliente_cep'),
    ]

    operations = [
        migrations.CreateModel(
            name='cliente_portabilidade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('orgao', models.CharField(blank=True, max_length=200, null=True)),
                ('n_beneficio', models.CharField(blank=True, max_length=200, null=True)),
                ('especie_beneficio', models.CharField(blank=True, max_length=100, null=True)),
                ('uf_beneficio', models.CharField(blank=True, max_length=2, null=True)),
                ('nome', models.CharField(max_length=200)),
                ('cpf', models.CharField(blank=True, max_length=14, null=True)),
                ('data_nasc', models.DateTimeField(blank=True, null=True)),
                ('natural', models.CharField(blank=True, max_length=200, null=True)),
                ('uf_natural', models.CharField(blank=True, max_length=2, null=True)),
                ('endereco', models.CharField(blank=True, max_length=200, null=True)),
                ('numero', models.CharField(blank=True, max_length=30, null=True)),
                ('complemento', models.CharField(blank=True, max_length=200, null=True)),
                ('bairro', models.CharField(blank=True, max_length=100, null=True)),
                ('cidade', models.CharField(blank=True, max_length=100, null=True)),
                ('uf_cidade', models.CharField(blank=True, max_length=2, null=True)),
                ('cep', models.CharField(blank=True, max_length=100, null=True)),
                ('tel', models.CharField(blank=True, max_length=20, null=True)),
                ('cel', models.CharField(blank=True, max_length=20, null=True)),
                ('mail', models.CharField(blank=True, max_length=200, null=True)),
                ('banco_atual', models.CharField(blank=True, max_length=200, null=True)),
                ('banco_prtador', models.CharField(blank=True, max_length=200, null=True)),
                ('ctt', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('quitacao', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('valor_parcela', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('liquido', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('banco_atual1', models.CharField(blank=True, max_length=200, null=True)),
                ('banco_prtador1', models.CharField(blank=True, max_length=200, null=True)),
                ('ctt1', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('quitacao1', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('valor_parcela1', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('liquido1', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('banco_atual2', models.CharField(blank=True, max_length=200, null=True)),
                ('banco_prtador2', models.CharField(blank=True, max_length=200, null=True)),
                ('ctt2', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('quitacao2', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('valor_parcela2', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('liquido2', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('banco_atual3', models.CharField(blank=True, max_length=200, null=True)),
                ('banco_prtador3', models.CharField(blank=True, max_length=200, null=True)),
                ('ctt3', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('quitacao3', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('valor_parcela3', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('liquido3', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('f_pagamento', models.CharField(blank=True, max_length=100, null=True)),
                ('banco', models.CharField(blank=True, max_length=100, null=True)),
                ('agencia', models.CharField(blank=True, max_length=100, null=True)),
                ('n_conta', models.CharField(blank=True, max_length=100, null=True)),
                ('t_conta', models.CharField(blank=True, max_length=100, null=True)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('data_cadastro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
