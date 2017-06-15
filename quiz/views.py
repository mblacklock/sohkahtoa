# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from operator import itemgetter
from itertools import groupby
from collections import Counter

from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse, JsonResponse

from topics.models import Subtopic
from models import Question, Score #, Answer

# Create your views here.

def get_question_list(request):
    question_list = []
    if request.method == "GET":
        subtopic = request.GET['subtopic']
        try:
            question_list = Question.objects.filter(subtopic__name=subtopic).filter(subtopic__is_active=True).order_by('level')
        except Question.DoesNotExist:
            question_list = []
        q_list_serial = list(question_list.values())
        for q in q_list_serial:
            q['subtopic'] = subtopic
        response = JsonResponse(q_list_serial, safe=False)

    return response

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
            score.save()         

        return HttpResponse('Success')
##        if question_list:
##            for q, s in zip(question_list, quiz_scores):
##
##                
##        question = Question.objects.get(slug=q).level
##        score = Score(commit=False)
##        score.user = user
##        score.subtopic = question.subtopic
##        score.level = question.level
##        score.score = 0 #update with calc
##        score.save()
            

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
