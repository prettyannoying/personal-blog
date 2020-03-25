from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
import uuid
from .unique_slug import unique_slugify
from tinymce.widgets import TinyMCE
# Create your models here.

class Post(models.Model):
	#author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	title=models.CharField(max_length=200)
	#formatting=models.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows':30}))
	blog_data=models.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows':30}))#models.TextField()
	date_posted=models.DateTimeField(default=timezone.now)
	published_date=models.DateTimeField(blank=True,null=True)
	slug=models.SlugField(max_length=250, unique=True)

	def publish(self):
		#self.slug=unique_slugify(self, self.title)
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		#self.slug=unique_slugify(self, self.title)
		self.save()
		return reverse('post-detail',kwargs={'slug':self.slug})

	def snippet(self):
		return self.blog_data[:100] 
