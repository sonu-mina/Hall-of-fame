from django import forms
from .models import *

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['url']
        labels = {'url':'YouTube_URL'}
        
class SearchForm(forms.Form):
    search_term = forms.CharField(max_length=300,label = 'Search for Video')
