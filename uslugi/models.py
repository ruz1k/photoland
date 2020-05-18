from django.db import models
from django.conf import settings
from django.utils import timezone

class Uslugi(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	price = models.IntegerField(null=True)
	image = models.ImageField(upload_to="media/uslugi", null=True)

	def publish(self):
		self.save()

		def __str__(self):
			return self.title

