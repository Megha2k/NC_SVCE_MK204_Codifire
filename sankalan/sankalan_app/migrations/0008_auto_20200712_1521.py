# Generated by Django 3.0.3 on 2020-07-12 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sankalan_app', '0007_auto_20200712_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='civilian_data',
            name='phone_no',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]