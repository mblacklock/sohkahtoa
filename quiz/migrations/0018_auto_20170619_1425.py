# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-19 13:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0017_auto_20170615_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='subtopic',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
