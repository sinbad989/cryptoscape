# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-02 03:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptodata', '0006_auto_20171231_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='block_time',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AlterField(
            model_name='data',
            name='genesis',
            field=models.CharField(default='Unknown', max_length=255),
        ),
    ]
