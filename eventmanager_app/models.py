from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    is_attended = models.BooleanField(default=False)
    reminder_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.title
        