# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_ID', models.IntegerField()),
                ('phase', models.CharField(choices=[('B', 'BEFORE'), ('C', 'RUNNING'), ('P', 'PENDING_SYSTEM_TEST'), ('S', 'SYSTEM_TEST'), ('F', 'FINISHED')], max_length=2)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
    ]
