# Generated by Django 3.2.5 on 2022-05-20 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User_Events',
            new_name='User_Event',
        ),
    ]