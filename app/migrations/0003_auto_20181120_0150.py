# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-19 22:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181120_0146'),
    ]

    operations = [
        migrations.AddField(
            model_name='newform',
            name='Update1',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='newform',
            name='Update2',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='newform',
            name='Update3',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='newform',
            name='Update4',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='newform',
            name='Update5',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='newform',
            name='Update6',
            field=models.TextField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='newform',
            name='Status',
            field=models.TextField(max_length=5000),
        ),
    ]
