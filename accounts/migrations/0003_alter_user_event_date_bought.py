# Generated by Django 3.2.5 on 2022-05-27 14:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_event_date_bought'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_event',
            name='date_bought',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 27, 14, 28, 5, 245174, tzinfo=utc)),
        ),
    ]
