# Generated by Django 3.0.3 on 2020-07-18 16:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sankalan_app', '0025_auto_20200718_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='civilian_data',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]