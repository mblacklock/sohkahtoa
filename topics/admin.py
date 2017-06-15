# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from topics.models import Subtopic, Topic, Year

# Register your models here.

class TopicInline(admin.TabularInline):
    model = Topic
    extra = 0
    prepopulated_fields = {'slug':('name',)}

class SubtopicInline(admin.TabularInline):
    model = Subtopic
    extra = 0
    prepopulated_fields = {'slug':('name',)}

class YearAdmin(admin.ModelAdmin):
    model = Year
    fields = ('year', 'is_active')
    list_display = fields
    inlines = [TopicInline]

class TopicAdmin(admin.ModelAdmin):
    model = Topic
    prepopulated_fields = {'slug':('name',)}
    fields = ('name','year','slug','is_active')
    list_display = fields
    search_fields = ['name']
    inlines = [SubtopicInline]

class SubtopicAdmin(admin.ModelAdmin):
    model = Subtopic
    prepopulated_fields = {'slug':('name',)}
    fields = ('name', 'slug', 'topic')
    list_display = fields
    search_fields = ['name']

admin.site.register(Year, YearAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Subtopic, SubtopicAdmin)
