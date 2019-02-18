from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
	#author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	title=models.CharField(max_length=200)
	blog_data=models.TextField()
	date_posted=models.DateTimeField(default=timezone.now)
	published_date=models.DateTimeField(blank=True,null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail',kwargs={'pk':self.pk})
