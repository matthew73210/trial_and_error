from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
# This is where classes are defined for the hello app.

class introduction(models.Model):
    name = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
