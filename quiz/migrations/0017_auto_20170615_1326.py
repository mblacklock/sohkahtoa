# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-15 12:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('topics', '0001_initial'),
        ('quiz', '0016_auto_20170614_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(default=1)),
                ('number_answered', models.IntegerField(default=0)),
                ('number_correct', models.IntegerField(default=0)),
                ('score', models.FloatField(default=0.0)),
                ('is_current', models.BooleanField(default=True)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('subtopic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topics.Subtopic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='user',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
