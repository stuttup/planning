from django.db import models
from django.utils import timezone

# Create your models here.
class Events(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_title = models.CharField(max_length=200)
    event_start = models.DateField(default=timezone.now)
    event_end = models.DateField(blank=True, null=True)
    resource = models.CharField(max_length=20)
    event_type = models.CharField(max_length=30)
    event_color = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.event_title
    

