import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'sohkahtoa.settings')

import django
django.setup()

from datetime import datetime

from topics.models import Subtopic, Topic, Year

def populate():

    whole_subtopics = [{"name": "Adding Whole"},
                       {"name": "Subtracting Whole"}]
    negative_subtopics = [{"name": "Adding Negatives"},
                       {"name": "Subtracting Negatives"}]

    temp81_subtopics = []
    temp82_subtopics = []
    temp91_subtopics = []
    temp92_subtopics = []

    seven_topics = {"Whole Numbers":{
                    "subtopics": whole_subtopics},
                    "Negative Numbers":{
                 "subtopics": negative_subtopics}
                }
    eight_topics = {"Temp 8 1":{
                     "subtopics": temp81_subtopics},
                    "Temp 8 2":{
                     "subtopics": temp82_subtopics}
                    }
    nine_topics = {"Temp 9 1":{
                     "subtopics": temp91_subtopics},
                   "Temp 9 2":{
                     "subtopics": temp92_subtopics}
                    }

    years = {7: {"topics": seven_topics},
             8: {"topics": eight_topics},
             9: {"topics": nine_topics}}

    for year, year_data in years.items():
        y = add_year(year)
        print("- Year " + str(year))
                          
        for topic, topic_data in year_data['topics'].items():
            t = add_topic(y, topic)
            print("- " + topic)
            
            for subtopic in topic_data["subtopics"]:
                add_subtopic(t, subtopic["name"])
                print("- " + subtopic['name'])

def add_year(year):
    y = Year.objects.get_or_create(year=year)[0]
    y.is_active = True
    y.save()
    return y

def add_topic(year, name):
    t = Topic.objects.get_or_create(year=year, name=name)[0]
    t.is_active = True
    t.save()
    return t

def add_subtopic(topic, name):
    s = Subtopic.objects.get_or_create(topic=topic, name=name)[0]
    #s.video_url
    s.is_active = True
    s.save()
    return s

if __name__ == '__main__':
    print('Starting Topics population script...')
    populate()
