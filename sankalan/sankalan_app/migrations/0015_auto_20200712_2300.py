# Generated by Django 3.0.3 on 2020-07-12 17:30

from django.db import migrations, models
import sankalan_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('sankalan_app', '0014_login_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='civilian_data',
            name='dob',
            field=models.DateField(validators=[sankalan_app.models.validate_date]),
        ),
    ]