# Generated by Django 3.2.5 on 2022-05-27 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_user_event_purchase_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_event',
            name='date_bought',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
