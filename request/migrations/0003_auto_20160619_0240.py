# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-19 02:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0002_auto_20160614_0500'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perrequest',
            old_name='per',
            new_name='perID',
        ),
    ]
