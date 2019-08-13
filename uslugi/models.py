from django.db import models
from django.conf import settings
from django.utils import timezone

class Uslugi(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	image = models.ImageField(upload_to="media/uslugi", null=True)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

		def __str__(self):
			return self.title

