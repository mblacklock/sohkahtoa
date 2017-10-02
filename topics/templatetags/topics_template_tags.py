from django import template
from topics.models import Subtopic, Topic, Year

register = template.Library()

@register.inclusion_tag('topics/year_list.html')
def get_year_list(year=None):
    year_list = Year.objects.order_by('year')
    return {'year_list': year_list,
            'act_year': year}

@register.inclusion_tag('topics/topic_list.html')
def get_topic_list(year=None, topic=None):
    topic_list = []
    if request.method == "GET":
        year_in = request.GET['year']
        try:
            topic_list = Topic.objects.filter(year__year=year_in)
        except Topic.DoesNotExist:
            topic_list = []
    return {'topic_list': topic_list,
            'act_topic': topic}

@register.inclusion_tag('topics/subtopic_list.html')
def get_subtopic_list(subtopic=None):
    subtopic_list = []
    if subtopic:
        try:
            subtopic_list = Subtopic.objects.filter(topic=subtopic.topic)
        except Subtopic.DoesNotExist:
            subtopic_list = []
    return {'topic_list': subtopic_list,
            'act_topic': subtopic}
