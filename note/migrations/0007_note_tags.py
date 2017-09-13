# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-13 14:46
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0006_auto_20170913_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='tags',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('work', 'Work'), ('home', 'Home'), ('school-college', 'School/College'), ('hobby', 'Hobby'), ('others', 'Others')], max_length=37, null=True),
        ),
    ]
