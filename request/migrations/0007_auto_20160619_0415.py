# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 04:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0006_auto_20160619_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perrequest',
            name='per_id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]
