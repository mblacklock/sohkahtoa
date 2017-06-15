# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.template.defaultfilters import slugify

# Create your models here.

class Year(models.Model):
    year = models.IntegerField(unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.year)

class Topic(models.Model):
    year = models.ForeignKey(Year)
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Topic, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Subtopic(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    video_url = models.URLField()
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Subtopic, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
