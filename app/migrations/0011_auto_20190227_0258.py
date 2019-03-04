# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-26 23:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20190227_0249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newform',
            old_name='Destination',
            new_name='ArrivalTime',
        ),
        migrations.RenameField(
            model_name='newform',
            old_name='Origin',
            new_name='Depaturetime',
        ),
        migrations.AddField(
            model_name='newform',
            name='GoodsTo',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='newform',
            name='GoodsareFrom',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='newform',
            name='ArrivalDate',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='newform',
            name='DepatureDate',
            field=models.CharField(max_length=2000),
        ),
    ]
