# Generated by Django 3.2.5 on 2022-05-30 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_organizer_society_instagram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizer',
            name='society_instagram',
            field=models.CharField(max_length=255),
        ),
    ]