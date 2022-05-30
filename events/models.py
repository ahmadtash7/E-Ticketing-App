from django.db import models
from django.conf import settings
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
# Create your models here.


class Organizer(models.Model):
    society = models.CharField(max_length=255,primary_key=True)
    society_instagram = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.society}'


class Event(models.Model):
    name = models.CharField(max_length=255,primary_key=True)
    organizer = models.ForeignKey(Organizer,on_delete=models.CASCADE,to_field='society')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    total_tickets = models.IntegerField()
    tickets_sold = models.IntegerField()
    tickets_left = models.IntegerField()
    ticket_price = models.IntegerField()
    event_poster = models.ImageField(default= settings.STATIC_URL+ 'images/down.jpg', upload_to='images/')
    email_sent = models.BooleanField(default=False)

    class Meta:
        ordering =['start_date']

    def __str__(self):
        return f'{self.name}'
