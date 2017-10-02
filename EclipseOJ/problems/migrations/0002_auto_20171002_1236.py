# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 07:06
from __future__ import unicode_literals

from django.db import migrations, models
import problems.models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problems',
            options={'verbose_name_plural': 'Problems'},
        ),
        migrations.AlterModelOptions(
            name='testcases',
            options={'verbose_name_plural': 'TestCases'},
        ),
        migrations.AlterField(
            model_name='testcases',
            name='testcase_body',
            field=models.FileField(upload_to=problems.models.testcases_directory_path),
        ),
    ]
