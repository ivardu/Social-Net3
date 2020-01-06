from feed.models import Feed, Comments, Like
from django.forms import ModelForm
from django import forms

class FeedForm(ModelForm):
	post = forms.CharField(label='Post')
	images = forms.ImageField(label='Photos')

	class Meta:
		model = Feed
		fields = ['post','images',]

class CommentForm(ModelForm):
	comments = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Comments'}))
	class Meta:
		model = Comments
		fields = ['comments']


class LikeForm(ModelForm):
	class Meta:
		model = Like
		fields = ['like']