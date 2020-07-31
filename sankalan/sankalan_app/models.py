from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.core.validators import MaxLengthValidator
from datetime import date
from django.utils import timezone
from datetime import datetime  
from django.core.exceptions import ValidationError

# Create your models here.

state_choices = [
	("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh","Arunachal Pradesh"),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland")
]

sex_choices = [("female","female"),("male","male"),("other","other")]

rating_choices = [("unhappy","unhappy"),("neutral","neutral"),("satisfied","satisfied")]

country_choice = [("India","India")]

class Contact(models.Model):
	fname = models.CharField(max_length=25)
	lname = models.CharField(max_length=25)
	state = models.CharField(max_length=40,choices=state_choices,default="Delhi")
	email = models.EmailField(max_length=35, default='')
	subject = models.TextField(max_length=250, default='')

class Feedback(models.Model):
	fname = models.CharField(max_length=25,blank=True,null=True)
	lname = models.CharField(max_length=25,blank=True,null=True)
	email = models.EmailField(max_length=35, default='',null=True,blank=True)
	subject = models.TextField(max_length=250, default='')
	rating = models.CharField(max_length=10,choices=rating_choices,default="satisfied")

def validate_date(dob):
    if dob > timezone.now().date():
        raise ValidationError("Date of birth cannot be in the future!")

class Civilian_data(models.Model):
	fname = models.CharField(max_length=25)
	lname = models.CharField(max_length=25)
	aadhaar_no = models.IntegerField(unique=True)
	dob = models.DateField(validators=[validate_date])
	sex = models.CharField(max_length=6,choices=sex_choices,default="female")
	email = models.EmailField(max_length=35, default='')
	mobile_no = models.IntegerField()
	address = models.TextField(max_length=100, default='')
	city = models.CharField(max_length=25)
	state = models.CharField(max_length=40,choices=state_choices,default="Delhi")
	country = models.CharField(max_length=5,choices=country_choice,default="India")
	occupation = models.CharField(max_length=25)
	family_members = models.PositiveIntegerField()
	date = models.DateTimeField(default=datetime.now, blank=True)

	class Meta:
		verbose_name_plural = "Civilian Data"

# validators=[MinLengthValidator(12),MaxLengthValidator(12)]
# validators=[MaxLengthValidator(10),MinLengthValidator(10)]

class Surveyor(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	fname = models.CharField(max_length=25)
	lname = models.CharField(max_length=25)
	surveyor_id = models.CharField(max_length=10)
	contact = models.IntegerField()
	email = models.EmailField(max_length=35, default='')
	sex = models.CharField(max_length=6,choices=sex_choices,default="female")
	aadhaar_no = models.IntegerField()
	photo = models.ImageField(upload_to='photos',default="")
	address = models.TextField(max_length=100, default='')
	city = models.CharField(max_length=25)
	state = models.CharField(max_length=40,choices=state_choices,default="Delhi")
	country = models.CharField(max_length=5,choices=country_choice,default="India")

	def __str__(self):
		return self.user.username

class Received_SMS(models.Model):
	aadhaar_no = models.IntegerField(unique=True)
	mobile_no = models.CharField(max_length=15)
	date = models.DateTimeField(default=datetime.now, blank=True)

	class Meta:
		verbose_name_plural = "Received SMS"

