from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from events.models import Event

# Create your models here.

class User_Account(models.Model):
    cms_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=200)
    contact_number = PhoneNumberField(default='+920000000000')
    password = models.CharField(max_length=200)
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.cms_id}'

class User_Event(models.Model):
    class Meta:
        unique_together = (('user_cms_id', 'EventName'),)

    user_cms_id = models.ForeignKey(User_Account,on_delete=models.CASCADE,to_field='cms_id')
    EventName = models.ForeignKey(Event,on_delete=models.CASCADE,to_field='name')

    def __str__(self):
        return f'{self.EventName} {self.user_cms_id}'
