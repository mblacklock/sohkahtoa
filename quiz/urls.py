from django.conf.urls import url

from quiz import views

app_name = 'quiz'
urlpatterns = [
    url(r'^question_list/$',views.get_question_list,name='question_list'),
    url(r'^update_scores/$',views.update_scores,name='update_scores'),
    #url(r'^post_scores/$',views.post_scores,name='post_scores'), USED FOR ANSWER MODEL
]
