from django.conf.urls import url

from topics import views

app_name = 'topics'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^topic_list/$',views.get_topic_list,name='topic_list'),
    url(r'^subtopic_list/$',views.get_subtopic_list,name='subtopic_list'),
    url(r'^search_list/$',views.search_topic,name='search_list'),
    #url(r'^topic/(?P<topic_name_slug>[\w\-]+)/$',views.show_topic,name='show_topic'),   # links to target page for topic
    url(r'^subtopic/(?P<subtopic_name_slug>[\w\-]+)/$',views.show_subtopic,name='show_subtopic'),

]
