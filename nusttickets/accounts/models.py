from django.db import models

# Create your models here.

class User(models.Model):
    cms_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=200)
