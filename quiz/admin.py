# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from quiz.models import Question, Score, SubtopicQuiz, TopicQuiz #Answer,

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    model = Question
    prepopulated_fields = {'slug':('name',)}
    list_display = ('id', 'name', 'slug', 'subtopic', 'get_topic', 'level', 'instances', 'is_active')

    def get_topic(self, obj):
        return obj.subtopic.topic.name
    get_topic.short_description = 'Topic'

class ScoreAdmin(admin.ModelAdmin):
    model = Score
    readonly_fields=('time',)
    list_display = ('user',
                    'subtopic',
                    'level',
                    'number_correct',
                    'number_answered',
                    'is_current','time')
    search_fields = ['user__username',]

##class AnswerAdmin(admin.ModelAdmin):
##    model = Answer
##    readonly_fields=('answer_time',)
##    fields = ('user', 'question', 'is_correct')
##    list_display = ('user', 'question', 'is_correct','answer_time')
##    search_fields = ['user__username','question__subtopic__name','question__subtopic__topic__name']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Score, ScoreAdmin)
#admin.site.register(Answer, AnswerAdmin)
admin.site.register(SubtopicQuiz)
admin.site.register(TopicQuiz)
