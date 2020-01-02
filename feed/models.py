from django.db import models
from user.models import SnetUser
from PIL import Image

# Create your models here.

def user_directory_path(instance, filename):
	return 'user_{0}/{1}'.format(instance.user.username, filename)

class Feed(models.Model):
	post = models.TextField()
	images = models.ImageField(upload_to=user_directory_path)
	date = models.DateTimeField(auto_now_add=True) 
	user = models.ForeignKey(SnetUser, on_delete=models.CASCADE)

	class Meta:
		ordering = ['-date']


	def save(self, *args, **kwargs):
		super().save(*args,**kwargs)
		img = Image.open(self.images.path)
		if img.width > 400 and img.height > 400:
			output_size = (400,400)
			img.thumbnail(output_size)
			img.save(self.images.path)