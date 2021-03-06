# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-19 11:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lavajato_controle', '0001_initial'),
        ('lavajato_cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='agenda',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pagamento', models.CharField(choices=[('1', 'Dinheiro'), ('2', 'Cartao Debito'), ('3', 'Cartao Credito'), ('4', 'Aberto'), ('5', 'Desmarcado')], max_length=1)),
                ('data', models.DateTimeField(blank=True, null=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_cadastro', models.DateTimeField(default=django.utils.timezone.now)),
                ('cli', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lavajato_cliente.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='servico_item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cancelado', models.CharField(choices=[('1', 'Nao'), ('2', 'Sim')], default='1', max_length=1)),
                ('data_cadastro', models.DateTimeField(default=django.utils.timezone.now)),
                ('func', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lavajato_controle.funcionario')),
                ('serv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lavajato_controle.servico')),
            ],
        ),
        migrations.AddField(
            model_name='agenda',
            name='item_servico',
            field=models.ManyToManyField(to='lavajato_agenda.servico_item'),
        ),
    ]
