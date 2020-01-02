from feed.models import Feed
from django.forms import ModelForm
from django import forms

class FeedForm(ModelForm):
	post = forms.CharField(label='Post')
	images = forms.ImageField(label='Photos')

	class Meta:
		model = Feed
		fields = ['post','images',]