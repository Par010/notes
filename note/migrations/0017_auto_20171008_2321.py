# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-08 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0016_auto_20171008_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkcontent',
            name='check_text',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.DeleteModel(
            name='Checktext',
        ),
    ]