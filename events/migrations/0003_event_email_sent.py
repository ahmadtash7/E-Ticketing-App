# Generated by Django 3.2.5 on 2022-05-28 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_event_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='email_sent',
            field=models.BooleanField(default=False),
        ),
    ]
