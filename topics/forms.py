from django import forms

##from topic.models import Subtopic, Topic
##
##class TopicForm(forms.ModelForm):
##    name = forms.CharField(max_length=Topic._meta.get_field('name').max_length, help_text="Please enter the topic name.")
##    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
##
##    class Meta:
##        model = Topic
##        fields = ('name',)
##
##class SubtopicForm(forms.ModelForm):
##    name = forms.CharField(max_length=Subtopic._meta.get_field('name').max_length, help_text="Please enter the subtopic name.")
##    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
##    video_url = forms.CharField(max_length=200, help_text="Please enter the url of the subtopic video.")
##
##    class Meta:
##        model = Subtopic
##        fields = ('name','video_url')
##
##    def clean(self):
##        cleaned_data = self.cleaned_data
##        url = cleaned_data.get('video_url')
##
##        if url and not (url.startswith('http://') or url.startswith('https://')):
##            url = 'http://' + url
##            cleaned_data['video_url'] = url
##
##            return cleaned_data

