# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-13 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20170613_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='question',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]
