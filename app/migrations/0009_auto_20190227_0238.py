# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-26 23:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20190227_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newform',
            name='ArrivalDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='newform',
            name='DepatureDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
