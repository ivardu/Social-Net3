from feed.models import Feed, Comments
from django.forms import ModelForm
from django import forms

class FeedForm(ModelForm):
	post = forms.CharField(label='Post')
	images = forms.ImageField(label='Photos')

	class Meta:
		model = Feed
		fields = ['post','images',]

class CommentForm(ModelForm):
	comments = forms.CharField(label=None, widget=forms.TextInput(attrs={'placeholder':'Comments'}))
	class Meta:
		model = Comments
		fields = ['comments']