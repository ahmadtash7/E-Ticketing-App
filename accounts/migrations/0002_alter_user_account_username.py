# Generated by Django 3.2.5 on 2022-05-30 07:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_account',
            name='username',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(999999), django.core.validators.MinValueValidator(111111)]),
        ),
    ]