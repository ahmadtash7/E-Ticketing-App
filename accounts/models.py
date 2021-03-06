from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from events.models import Event
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.utils.timezone import now

# Create your models here.

class User_Account(AbstractUser):
    id = None
    last_login = None
    username = models.IntegerField(primary_key=True)

    # first_name = models.CharField(max_length=200)
    # last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    contact_number = PhoneNumberField(default='+920000000000')
    # password = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.username}'

class User_Event(models.Model):
    class Meta:
        unique_together = (('user_username', 'EventName'),)

    user_username = models.ForeignKey(User_Account,on_delete=models.CASCADE,to_field='username')
    EventName = models.ForeignKey(Event,on_delete=models.CASCADE,to_field='name')

    BOUGHT = 'B'
    RESERVED = 'R'

    ue_choices = [(BOUGHT,'Bought'),(RESERVED,'RESERVED')]
    date_bought = models.DateTimeField()

    purchase_type = models.CharField(max_length=200,choices=ue_choices)

    def __str__(self):
        return f'{self.EventName} {self.user_username}'
