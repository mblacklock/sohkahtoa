from django.conf.urls import url

from targets import views

app_name = 'targets'
urlpatterns = [
    url(r'^topic/(?P<topic_name_slug>[\w\-]+)/$',views.show_topic,name='show_topic'),
]
