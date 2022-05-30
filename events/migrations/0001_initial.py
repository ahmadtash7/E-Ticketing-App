# Generated by Django 3.2.5 on 2022-05-30 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('society', models.CharField(max_length=255, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('total_tickets', models.IntegerField()),
                ('tickets_sold', models.IntegerField()),
                ('tickets_left', models.IntegerField()),
                ('ticket_price', models.IntegerField()),
                ('event_poster', models.ImageField(default='/static/images/down.jpg', upload_to='images/')),
                ('email_sent', models.BooleanField(default=False)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.organizer')),
            ],
            options={
                'ordering': ['start_date'],
            },
        ),
    ]
