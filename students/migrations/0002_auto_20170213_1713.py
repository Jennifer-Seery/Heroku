# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-13 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]
