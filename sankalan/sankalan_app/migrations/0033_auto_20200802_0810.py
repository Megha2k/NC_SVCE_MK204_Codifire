# Generated by Django 3.0.3 on 2020-08-02 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sankalan_app', '0032_auto_20200802_0809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='civilian_data',
            name='country',
            field=models.CharField(blank=True, choices=[('India', 'India')], default='India', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='civilian_data',
            name='state',
            field=models.CharField(blank=True, choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland')], default='Delhi', max_length=40, null=True),
        ),
    ]
