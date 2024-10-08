# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 05:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirewallRequest',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('service', models.CharField(blank=True, max_length=100)),
                ('protocol', models.GenericIPAddressField()),
                ('action', models.BooleanField(default=True)),
                ('log', models.BooleanField(default=True)),
                ('scheduled', models.BooleanField(default=False)),
                ('schedule_date', models.DateField(default=datetime.datetime.today)),
                ('rule_desc', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PERRequest',
            fields=[
                ('per', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='address_book',
            new_name='AddressBook',
        ),
        migrations.RenameModel(
            old_name='address_set',
            new_name='AddressSet',
        ),
        migrations.RenameModel(
            old_name='app_req',
            new_name='ApplicationRequest',
        ),
        migrations.RenameModel(
            old_name='gtm_req',
            new_name='GTMRequest',
        ),
        migrations.RenameModel(
            old_name='ltm_req',
            new_name='LTMRequest',
        ),
        migrations.RenameModel(
            old_name='ssl_req',
            new_name='SSLRequest',
        ),
        migrations.RemoveField(
            model_name='fw_req',
            name='address_set',
        ),
        migrations.RemoveField(
            model_name='per_req',
            name='app_req',
        ),
        migrations.RemoveField(
            model_name='per_req',
            name='fw_req',
        ),
        migrations.RemoveField(
            model_name='per_req',
            name='gtm_req',
        ),
        migrations.RemoveField(
            model_name='per_req',
            name='ltm_req',
        ),
        migrations.RemoveField(
            model_name='per_req',
            name='ssl_req',
        ),
        migrations.RenameField(
            model_name='addressbook',
            old_name='address_set',
            new_name='AddressSet',
        ),
        migrations.RenameField(
            model_name='gtmrequest',
            old_name='address_set',
            new_name='AddressSet',
        ),
        migrations.DeleteModel(
            name='fw_req',
        ),
        migrations.DeleteModel(
            name='per_req',
        ),
        migrations.AddField(
            model_name='perrequest',
            name='ApplicationRequest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.ApplicationRequest'),
        ),
        migrations.AddField(
            model_name='perrequest',
            name='FirewallRequest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.FirewallRequest'),
        ),
        migrations.AddField(
            model_name='perrequest',
            name='GTMRequest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.GTMRequest'),
        ),
        migrations.AddField(
            model_name='perrequest',
            name='LTMRequest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.LTMRequest'),
        ),
        migrations.AddField(
            model_name='perrequest',
            name='SSLRequest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.SSLRequest'),
        ),
        migrations.AddField(
            model_name='firewallrequest',
            name='AddressSet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.AddressSet'),
        ),
    ]
