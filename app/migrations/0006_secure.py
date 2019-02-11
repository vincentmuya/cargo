# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-11 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190204_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Secure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DepositorName', models.CharField(max_length=2000)),
                ('ReceiverName', models.CharField(max_length=2000)),
                ('TrackNo', models.CharField(max_length=2000)),
                ('Origin', models.CharField(max_length=2000)),
                ('Destination', models.CharField(max_length=2000)),
                ('TypeOfShipment', models.CharField(max_length=2000)),
                ('NatureOfGoods', models.TextField(max_length=5000)),
                ('Status', models.TextField(max_length=5000)),
            ],
        ),
    ]