from django.db import models
from django.conf import settings

class Shablon(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	image = models.ImageField(upload_to="media/image", null=True)