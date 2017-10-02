# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from operator import itemgetter
from itertools import groupby
from collections import Counter

import random, math

from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse

from topics.models import Subtopic, Topic
from models import Question, Score, TopicQuiz #, Answer

# Create your views here.

def get_question_list(request):
    q_list_serial_instances = []
    if request.method == "GET":
        level = request.GET['level']
        topicQuiz = request.GET['topicQuiz']
        if topicQuiz == 'False':
            subtopic = request.GET['subtopic']
            try:
                question_list = Question.objects.filter(subtopic__name=subtopic).filter(subtopic__is_active=True).filter(level=level).order_by('level')
            except Question.DoesNotExist:
                question_list = []
        else:
            subtopic = request.GET['subtopic']
            try:
                topic = Subtopic.objects.get(name=subtopic).topic
                try:
                    question_list = Question.objects.filter(subtopic__topic=topic).filter(subtopic__is_active=True).order_by('level')
                except Question.DoesNotExist:
                    question_list = []
            except Subtopic.DoesNotExist:
                question_list = []
        q_list_serial = list(question_list.values())
        for i in range(len(q_list_serial)):
            q_list_serial[i]['subtopic'] = question_list[i].subtopic.name
            q_list_serial[i]['subtopic_slug'] = question_list[i].subtopic.slug

        ## Question list according to instances
        for q in q_list_serial:
            for i in range(q['instances']):
                q_list_serial_instances.append(q)
        
        ## Change instances for topic quiz depending on out_of
        if topicQuiz == 'True':                
            topic_quiz = TopicQuiz.objects.get(topic=topic)
            out_of = topic_quiz.out_of

            # generates random list retaining original order
            if len(q_list_serial_instances) > out_of:
                q_list_serial_instances = [ q_list_serial_instances[i] for i in sorted(random.sample(xrange(len(q_list_serial_instances)), out_of)) ]
        ##
    
    response = JsonResponse(q_list_serial_instances, safe=False)
    
    return response

def active_levels(request):
    if request.method == 'GET':
        user = request.user
        subtopic = request.GET['subtopic']
        level = 1
        try:
            scores = Score.objects.filter(user__username=user).filter(is_current=True).filter(score__gte=0.6)
            for score in scores:
                if score.level > level:
                    level = score.level
        except Score.DoesNotExist:
            level = 1
        print(level)
        return JsonResponse({'level': level})

def update_scores(request):

    if request.method == "POST":
        #question_list = request.POST.getlist('question_list[]')
        subtopic_list = request.POST.getlist('subtopic_list[]')
        level_list = request.POST.getlist('level_list[]')
        quiz_scores = request.POST.getlist('score_list[]')
        user = request.user

        totals_list = []
        for j in range(len(subtopic_list)):
            subtopic_level_answered, subtopic_level_correct = 0, 0
            for i in range(len(subtopic_list)):
                if subtopic_list[i] == subtopic_list[j] and level_list[i] == level_list[j]:
                    subtopic_level_answered += 1
                    if str(quiz_scores[i]) == '1':
                        subtopic_level_correct += 1
            component = {'subtopic': subtopic_list[j],
                         'level': level_list[j],
                         'answered': subtopic_level_answered,
                         'correct': subtopic_level_correct}
            if component not in totals_list:
                totals_list.append(component)

        for total in totals_list:
            subtopic = Subtopic.objects.get(name=total['subtopic'])
            try:
                current_score = Score.objects.get(
                        user=user,
                        subtopic=subtopic,
                        level=int(total['level']),
                        is_current=True)
            except Score.DoesNotExist:
                current_score = None
            if current_score:
                cur_ans = current_score.number_answered
                cur_cor = current_score.number_correct
                current_score.is_current = False
                current_score.save()
            else:
                cur_ans = 0
                cur_cor = 0
                
            score = Score(user=user,
                          subtopic=subtopic,
                          level=int(total['level']))
            score.number_answered = cur_ans + total['answered']
            score.number_correct = cur_cor + total['correct']
            # score = % of correct, history independent
            score.score = total['correct']/float(total['answered'])
            score.save()

        return HttpResponse('Success')
            

## THIS IS FOR THE NOW REMOVED ANSWER MODEL
##def post_scores(request):
##    scores = []
##    if request.method == "POST":
##        question_list = request.POST.getlist('question_list[]')
##        scores = request.POST.getlist('scores[]')
##        user = request.user
##    if question_list:
##        for q, s in zip(question_list, scores):
##            question = Question.objects.get(slug=q)
##            answer = Answer(question=question, is_correct=s, user=user)
##            answer.save()
##    
##    return HttpResponse('Success')
