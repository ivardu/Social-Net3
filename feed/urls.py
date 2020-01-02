from django.urls import path
from feed import views as feed_view

app_name = 'feed'

urlpatterns = [
	path('',feed_view.home, name='home'),
	path('feed/',feed_view.feedview, name='feed'),
	path('feedit/<int:pk>/',feed_view.feededit, name='feedit'),
	path('myposts/<int:pk>/',feed_view.PostListView.as_view(), name='myposts'),
]