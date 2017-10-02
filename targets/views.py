# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from operator import itemgetter

from django.shortcuts import render

from quiz.models import Score
from topics.models import Subtopic, Topic

# Create your views here.

def show_topic(request, topic_name_slug):

    topic = None
    subtopics = None
    
    if request.method == 'GET':
        try:
            user = request.user
        except User.DoesNotExist:
            user = None
            
        if user:
            try:
                topic = Topic.objects.get(slug=topic_name_slug)
            except Topic.DoesNotExist:
                topic = None

        if topic:
            try:
                subtopics = Subtopic.objects.filter(topic=topic)
            except Subtopic.DoesNotExist:
                subtopics = None

        if subtopics:
            sub_scores = getSubtopicScores(user, topic, subtopics)
            average_sub_scores = getAverageSubtopicScores(subtopics)
            ranked_subtopics = rankSubtopics(sub_scores, average_sub_scores)

    context = {'topic': topic,
               'scores': sub_scores,
               'averages': average_sub_scores}
    
    return render(request, 'targets/topic.html', context)

def getSubtopicScores(user, topic, subtopics):

    try:
        scores = Score.objects.filter(user=user).filter(is_current=True).filter(subtopic__topic=topic)
    except Score.DoesNotExist:
        scores = None

    if scores:
        sub_scores = []
        for sub in subtopics:
            temp_score = None
            temp_score = scores.filter(subtopic=sub)
            if temp_score.count() > 0 and sub.is_quiz is False: # figure out how to deal with topic quiz seperately
                temp_sub_score = 0
                for s in temp_score:
                    temp_sub_score += s.level * s.score
                sub_scores.append({'subtopic': sub,'score': temp_sub_score/6})
            else:
                sub_scores.append({'subtopic': sub,'score': 0.})
        return sub_scores

def getAverageSubtopicScores(subtopics):

    average_sub_scores = []

    for sub in subtopics:
        s_objects = Score.objects.filter(is_current=True).filter(subtopic=sub)
        sub_score = 0
        n_scores = s_objects.count()
        if n_scores > 0:
            levels = s_objects.values('level')
            scores = s_objects.values('score')
            for i in range(len(levels)):
                sub_score += levels[i]['level'] * scores[i]['score']
            sub_score = sub_score / float(n_scores * 6)
                           
        average_sub_scores.append({'subtopic': sub, 'average_score': sub_score})

    return average_sub_scores                       

##def rankSubtopics(sub_scores, average_sub_scores):
##    scores = []
##    for i in range(len(sub_scores)):
##        scores.append({sub_scores[i]['subtopic'],
##                       sub_scores[i]['subtopic'] 
