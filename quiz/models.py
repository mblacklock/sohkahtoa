# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from topics.models import Subtopic, Topic

# Create your models here.

class SubtopicQuiz(models.Model):
    subtopic = models.OneToOneField(Subtopic)
    out_of = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Subtopic Quizzes'

    def __str__(self):
        return str(self.subtopic.name)

class TopicQuiz(models.Model):
    topic = models.OneToOneField(Topic)
    out_of = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Topic Quizzes'

    def __str__(self):
        return str(self.topic.name)

class Question(models.Model):
    subtopic = models.ManyToManyField(Subtopic)
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    level = models.IntegerField(blank=False, default=1)
    instances = models.IntegerField(blank=False, default=1)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = self.name.replace(" ", "_").lower()
        super(Question, self).save(*args, **kwargs)

    def get_subtopics(self):
        return "\n".join([s.name for s in self.subtopic.all()])
    get_subtopics.short_description = 'Subtopics'
    #get_subtopics.admin_order_field = 'subtopic'

    def __str__(self):
        return str(self.name)

class Score(models.Model):
    user = models.ForeignKey(User)
    subtopic = models.ForeignKey(Subtopic)
    level = models.IntegerField(blank=False, default=1)
    number_answered = models.IntegerField(blank=False, default=0)
    number_correct = models.IntegerField(blank=False, default=0)
    score = models.FloatField(blank=False, default=0.)
    is_current = models.BooleanField(default=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username) + ' - ' + str(self.subtopic.name) \
               + ' - ' + str(self.level)

##class Answer(models.Model):
##    user = models.ForeignKey(User)
##    question = models.ForeignKey(Question)
##    is_correct = models.BooleanField(default=False)
##    answer_time = models.DateTimeField(auto_now_add=True)
##
##    def __str__(self):
##        return str(self.question.id)
    
