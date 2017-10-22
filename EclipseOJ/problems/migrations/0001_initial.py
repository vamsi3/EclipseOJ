# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 07:38
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import problems.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_ID', models.CharField(max_length=10, unique=True)),
                ('letter', models.CharField(max_length=1, validators=[django.core.validators.RegexValidator('^[A-Z]$', 'Only a captial letter is allowed.')], verbose_name='Problem ID')),
                ('name', models.CharField(max_length=40)),
                ('body', models.TextField()),
                ('timelimit', models.FloatField(default=1)),
                ('marks', models.IntegerField(default=0)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contests.Contest')),
            ],
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testcase_ID', models.PositiveIntegerField()),
                ('input_file', models.FileField(upload_to=problems.models.testcases_input_path)),
                ('output_file', models.FileField(upload_to=problems.models.testcases_output_path)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.Problem')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='testcase',
            unique_together=set([('problem', 'testcase_ID')]),
        ),
    ]
