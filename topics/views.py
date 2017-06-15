# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.template.defaultfilters import slugify

from collections import OrderedDict
from itertools import chain

from topics.models import Subtopic, Topic, Year

# Create your views here.

def index(request):

    context = {}
    
    return render(request, 'topics/index.html', context)

def get_topic_list(request):
    topic_list = []
    if request.method == "GET":
        year_in = request.GET['year']
        try:
            topic_list = Topic.objects.filter(year__year=year_in)
        except Topic.DoesNotExist:
            topic_list = []

    return render(request, 'topics/topic_list.html', {'topic_list': topic_list})

def get_subtopic_list(request):
    subtopic_list = []
    if request.method == "GET":
        topic = request.GET['topic']
        try:
            subtopic_list = Subtopic.objects.filter(topic__name=topic)
        except Subtopic.DoesNotExist:
            subtopic_list = []

    return render(request, 'topics/subtopic_list.html', {'topic_list': subtopic_list})

def search_topic(request):
    starts_with = ''
    max_results = 100
    topic_list = [] # replace with X.objects.all() to show list before typing
    subtopic_list = []
    overall_list = []

    if request.method == 'GET':
        starts_with = request.GET['suggestion']
    
    if starts_with:
        topic_list = Subtopic.objects.filter(topic__name__icontains=starts_with)
        subtopic_list = Subtopic.objects.filter(name__icontains=starts_with)
        overall_list = list(chain(topic_list, subtopic_list))
        print(subtopic_list)
        overall_list = list(OrderedDict.fromkeys(overall_list))
    if max_results > 0:
        if len(overall_list) > max_results:
            overall_list = overall_list[:max_results]
    return render(request, 'topics/subtopic_list.html', {'topic_list': overall_list, 'search':True})

def show_subtopic(request, subtopic_name_slug):
    try:
        subtopic = Subtopic.objects.get(slug=subtopic_name_slug)

        context = {
            'subtopic': subtopic,
            'VIDEO_LINK': 'topics/videos/{}.mp4'.format(subtopic.slug)
            }
    except:
        context = {
            'subtopic': None,
            }
    return render(request, 'topics/subtopic.html', context)
