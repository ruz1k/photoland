from django.db import models

class PrimerImage(models.Model):
    title = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to="media/primeri", null=True)

    def publish(self):
        self.save()

        def __str__(self):
            return self.title
