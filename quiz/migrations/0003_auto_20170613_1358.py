# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-13 12:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20170613_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='question',
            name='object_id',
        ),
        migrations.AddField(
            model_name='question',
            name='quiz_subtopic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.SubtopicQuiz'),
        ),
        migrations.AddField(
            model_name='question',
            name='quiz_topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.TopicQuiz'),
        ),
    ]
