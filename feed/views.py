from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView 
from django.views.generic import ListView
from feed.forms import FeedForm
from feed.models import Feed
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
	obj = Feed.objects.all()
	return render(request, 'feed/home.html', {'feed_list':obj})


@login_required
def feedview(request):
	obj = Feed.objects.all()
	if request.method == 'POST':
		form = FeedForm(request.POST, request.FILES)
		if form.is_valid():
			feed = form.save(commit=False)
			feed.user = request.user
			feed.save()
			return HttpResponseRedirect(reverse('feed:feed'))
	else:
		form = FeedForm()
	return render(request,'feed/feed.html',{'form':form,'feed_list':obj})


def feededit(request, pk):
	feed = Feed.objects.get(pk=pk)
	if request.method == 'POST':
		form = FeedForm(request.POST, instance=feed)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('feed:myposts',args=(feed.user_id,)))
	else:
		form = FeedForm(instance=feed)

	return render(request, 'feed/feedit.html', {'form':form})


class PostListView(ListView):
	model = Feed
	template_name = 'feed/myposts.html'
	context_object_name = 'feed'
	paginate_by = 2

	def get_queryset(self):
		return Feed.objects.filter(user_id=self.kwargs['pk'])



