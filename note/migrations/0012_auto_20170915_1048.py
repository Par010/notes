# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-15 05:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0011_auto_20170913_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='create_date',
            field=models.DateField(default=datetime.date(2017, 9, 15)),
        ),
    ]
