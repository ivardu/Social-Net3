from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

# Create your models here.

class SnetUser(AbstractUser):
	GENDER_CHOICES = (
			('M','Male'),
			('F','Female'),
			('T','Trans'),
		)
	dob = models.DateField()
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

	def __str__(self):

		return f'{self.username}'

def profile_img_dir(instance, filename):
	return 'profile_img_{0}/{1}'.format(instance.user.username, filename)

class Profile(models.Model):
	user = models.OneToOneField(SnetUser, on_delete=models.CASCADE)
	p_img = models.ImageField(default='default.png/', upload_to=profile_img_dir)

	def save(self, *args, **kwargs):
		super().save()
		img = Image.open(self.p_img.path)
		if img.width>400 and img.height >400:
			output = (400,400)
			img = img.resize(output)
			img.save(self.p_img.path)

	def __str__(self):

		return f'{self.user}'


