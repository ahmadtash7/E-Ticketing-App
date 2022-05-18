from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255,primary_key=True)
    organizer = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    total_tickets = models.IntegerField()
    tickets_sold = models.IntegerField()
    tickets_left = models.IntegerField()
    ticket_price = models.IntegerField()
