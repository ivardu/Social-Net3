from django.shortcuts import render
from django.views.generic.edit import FormView
from user.forms import SignUpForm, ProfileForm, UserUpdateForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from user.models import SnetUser

# Create your views here.

# class SignUpView(FormView):
# 	form_class = SignUpForm
# 	template_name = 'user/register.html'
# 	success_url = reverse_lazy('login')


# 	def form_valid(self, form):
# 		# form = SignUpForm(self.request.POST)
# 		# form.save()
# 		response = super().form_valid(form)
# 		return HttpResponse(response)

# 	def form_invalid(self, form):
# 		response = super().form_invalid(form)
# 		return HttpResponse(response)


def register(request):

	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('login'))
	else:
		form = SignUpForm()

	return render(request, 'user/register.html',{'form':form})

@login_required
def profile(request):
	if request.method == 'POST':
		pform = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
		uform = UserUpdateForm(request.POST, instance=request.user)

		if pform.is_valid() and uform.is_valid():
			pform.save()
			uform.save()

			return HttpResponseRedirect(reverse('profile'))
		# return HttpResponse(request.FILES)
	else:
		pform = ProfileForm(instance=request.user.profile)
		uform = UserUpdateForm(instance=request.user)

	return render(request, 'user/profile.html', {'pform':pform, 'uform':uform})


def rprofile(request, pk):
	obj = SnetUser.objects.get(pk=pk)
	# pform = ProfileForm(instance=request.user.profile)
	uform = UserUpdateForm(instance=obj)

	return render(request, 'user/rprofile.html', {'uform':uform, 'obj':obj})