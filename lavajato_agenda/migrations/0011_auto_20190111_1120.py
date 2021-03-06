# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-11 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lavajato_agenda', '0010_auto_20190109_1232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conta_parcelada',
            name='parcelas',
        ),
        migrations.RemoveField(
            model_name='conta_parcelada',
            name='referente',
        ),
        migrations.AddField(
            model_name='agenda',
            name='parcelas',
            field=models.ManyToManyField(to='lavajato_agenda.parcela'),
        ),
        migrations.AddField(
            model_name='agenda',
            name='total_parcelas',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.DeleteModel(
            name='conta_parcelada',
        ),
    ]
