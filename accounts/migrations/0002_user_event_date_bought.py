# Generated by Django 3.2.5 on 2022-05-27 14:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_event',
            name='date_bought',
            field=models.DateTimeField(default=datetime.date(2022, 5, 27)),
        ),
    ]