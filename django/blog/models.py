from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return 'id: '+str(self.id)+' title:'+self.title


class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	content = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return 'id: '+str(self.id)+' title:'+self.content