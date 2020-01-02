from user.models import SnetUser, Profile
from django.contrib.auth.forms import UserCreationForm
from django import forms

class SignUpForm(UserCreationForm):
	GENDER_CHOICES = (
			('M','Male'),
			('F','Female'),
			('T','Trans'),
		)
	first_name = forms.CharField()
	last_name = forms.CharField()
	gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Gender')
	dob = forms.DateField(label='Date of Birth', input_formats=['%d/%m/%Y'])
	email = forms.CharField(required=True, widget=forms.EmailInput())
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
	class Meta:
		model = SnetUser
		fields = ['username',
		'first_name','last_name','email','dob','gender']
		help_texts = {
			'username':None,
		}

class ProfileForm(forms.ModelForm):
	p_img = forms.ImageField(label='Profile Photo')

	class Meta:
		model = Profile
		fields = ['p_img']

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = SnetUser
		fields = ['email','first_name', 'last_name', 'dob']
