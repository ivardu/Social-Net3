from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView 
from django.views.generic import ListView
from feed.forms import FeedForm, CommentForm, LikeForm
from feed.models import Feed
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def home(request):
	obj = Feed.objects.all()
	return render(request, 'feed/home.html', {'feed_list':obj})


@login_required
def feedview(request):
	obj = Feed.objects.all()
	page = request.GET.get('page',1)
	paginator = Paginator(obj, 5)
	# commlist = 
	try:
		pages = paginator.page(page)
	except PageNotAnInteger:
		pages = paginator.page(1)
	except EmptyPage:
		pages = paginator.page(paginator.num_pages)
	# Validating the Feed Post Data and Comment Data
	if request.method == 'POST':
		form = FeedForm(request.POST, request.FILES)
		comment = CommentForm(request.POST)
		like = LikeForm(request.POST)
		feed_obj = get_object_or_404(Feed, pk=request.POST.get('items_id'))
		already_liked = feed_obj.like_set.filter(user=request.user) and True or False
		# Feed Form Data 
		if form.is_valid():
			feed = form.save(commit=False)
			feed.user = request.user
			feed.save()
			return HttpResponseRedirect(reverse('feed:feed'))
		# Comment Form Data 
		elif comment.is_valid():
			comment = comment.save(commit=False)
			comment.feed = feed_obj
			comment.user = request.user
			comment.save()
			return HttpResponseRedirect(reverse('feed:feed'))
		# Like Form Data 
		elif like.is_valid() and already_liked == False:
			like_model = like.save(commit=False)
			like_model.like = like.cleaned_data['like']
			like_model.user = request.user
			like_model.post = feed_obj
			like_model.save()
			return HttpResponseRedirect(reverse('feed:feed'))
		else:
			return HttpResponseRedirect(reverse('feed:feed'))
	else:
		form = FeedForm()
		comment = CommentForm()
		# like = LikeForm()
	return render(request,'feed/feed.html',locals())
# {'form':form,'comment':comment,'like':like, 'pages':pages}

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



