# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-12-20 12:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lavajato_agenda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='conta_parcelada',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('parcelas_total', models.IntegerField()),
                ('data_cadastro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='parcela',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(choices=[('1', 'Em Aberto'), ('2', 'Paga')], max_length=1)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='conta_parcelada',
            name='parcelas',
            field=models.ManyToManyField(to='lavajato_agenda.parcela'),
        ),
        migrations.AddField(
            model_name='conta_parcelada',
            name='referente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lavajato_agenda.agenda'),
        ),
    ]
