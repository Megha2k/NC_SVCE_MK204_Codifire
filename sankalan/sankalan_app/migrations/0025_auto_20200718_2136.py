# Generated by Django 3.0.3 on 2020-07-18 16:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sankalan_app', '0024_civilian_data_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='civilian_data',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
