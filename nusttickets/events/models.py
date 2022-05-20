from django.db import models

# Create your models here.


class Organizer(models.Model):
    society = models.CharField(max_length=255,primary_key=True)

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


    def __str__(self):
        return f'{self.name} {self.organizer}'
