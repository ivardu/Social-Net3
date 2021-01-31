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

	def __str__(self):
		return f'{self.post}'

class Comments(models.Model):
	comments = models.CharField(max_length=255)
	parent_comment = models.ForeignKey('self', null=True, on_delete=models.CASCADE, related_name='child_comments')
	feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
	user = models.ForeignKey(SnetUser, on_delete=models.CASCADE, related_name='+')
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.comments}'

	class Meta:
		ordering = ['-date']

class Like(models.Model):
	like = models.IntegerField()
	user = models.ForeignKey(SnetUser, on_delete=models.CASCADE)
	post = models.ForeignKey(Feed, on_delete=models.CASCADE)