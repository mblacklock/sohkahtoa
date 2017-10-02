# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-19 13:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
        ('quiz', '0018_auto_20170619_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('level', models.IntegerField(default=1)),
                ('instances', models.IntegerField(default=1)),
                ('is_active', models.BooleanField(default=True)),
                ('subtopic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topics.Subtopic')),
            ],
        ),
    ]
