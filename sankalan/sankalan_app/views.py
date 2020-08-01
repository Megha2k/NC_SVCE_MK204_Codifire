from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from sankalan_app.models import Contact
from sankalan_app.models import Feedback
from sankalan_app.models import Civilian_data
from sankalan_app.models import Surveyor
from sankalan_app.models import Received_SMS
from django.contrib.auth.decorators import login_required
from twilio.rest import Client
from django.conf import settings
import os
from twilio.http.http_client import TwilioHttpClient
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse

# Create your views here.
def index(request):

	if request.method == "POST":

		if 'login_form' in request.POST:

			username = request.POST["username"]
			password = request.POST["password"]

			user = authenticate(username=username, password=password)

			if user and not user.is_staff:
				login(request,user)
				return HttpResponseRedirect("/data_entry_page")
			elif user and user.is_staff:
				login(request,user)
				return HttpResponseRedirect("/register")

			else:
				return render(request,'index.html',{"status":"Invalid username or password!"})

		if 'contact_form' in request.POST:

			fname = request.POST["fname"]
			lname = request.POST["lname"]
			state = request.POST["state"]
			email = request.POST["email"]
			subject = request.POST["subject"]

			data = Contact(fname=fname,lname=lname,state=state,email=email,subject=subject)
			data.save()

			return render(request,'contact_form_redirect.html')

		elif 'feedback_form' in request.POST:

			fname = request.POST["fname"]
			lname = request.POST["lname"]
			email = request.POST["email"]
			subject = request.POST["subject"]
			rating = request.POST["rating"]

			data = Feedback(fname=fname,lname=lname,email=email,subject=subject,rating=rating)
			data.save()

			return render(request,'feedback_form_redirect.html')

	return render(request,'index.html')

@login_required
def data_entry(request):

	surveyor_data = Surveyor.objects.get(user__id=request.user.id)
	context = {}
	context["surveyor_data"] = surveyor_data
	proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})

	if 'data_entry_form' in request.POST:

	    fname = request.POST["fname"]
	    lname = request.POST["lname"]
	    aadhaar_no = request.POST["aadhaar_no"]
	    dob = request.POST["dob"]
	    sex = request.POST["sex"]
	    email = request.POST["email"]
	    mobile_no = request.POST["mobile_no"]
	    address = request.POST["address"]
	    city = request.POST["city"]
	    state = request.POST["state"]
	    country = request.POST["country"]
	    occupation = request.POST["occupation"]
	    family_members = request.POST["family_members"]

	    data = Civilian_data(fname=fname,lname=lname,aadhaar_no=aadhaar_no,dob=dob,sex=sex,email=email,mobile_no=mobile_no,address=address,city=city,state=state,country=country,occupation=occupation,family_members=family_members)
	    data.save()
	    obj1 = Civilian_data.objects.get(aadhaar_no = aadhaar_no)
	    fnameobj1 = obj1.fname
	    lnameobj1 = obj1.lname
	    aadhaar_noobj1 = obj1.aadhaar_no
	    mob_noobj1 = "+91"+ str(obj1.mobile_no)
	    DOBobj1 = obj1.dob
	    sexobj1 = obj1.sex
	    emailobj1 = obj1.email
	    addressobj1 = obj1.address
	    cityobj1 = obj1.city
	    stateobj1 = obj1.state
	    occuobj1 = obj1.occupation
	    fam_memobj1 = obj1.family_members
        surveyor_mob_no = surveyor_data.contact
	    message_to_broadcast = ("Hello \n Data entered is \n Name = %s %s , \n aadhar num = %d, DOB = %s, Sex = %s, Email = %s, Address = %s  %s %s , Occupation = %s, FamilyMem NO = %s. \n If data entered is incorect, then contact your surveyor with +91%s" %(fnameobj1, lnameobj1, aadhaar_noobj1, DOBobj1, sexobj1, emailobj1, addressobj1, cityobj1, stateobj1, occuobj1, fam_memobj1, surveyor_mob_no))
	    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN, http_client=proxy_client)
	    if obj1.aadhaar_no and obj1.mobile_no:
	        client.messages.create(to=mob_noobj1, from_=settings.TWILIO_NUMBER, body=message_to_broadcast)

	    return render(request,'data_entry_form_redirect.html')
	else:
	    return render(request,'data_entry.html',context)

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect("/homepage")

@login_required
def register(request):

	if 'registration_form' in request.POST:
		fname = request.POST["fname"]
		lname = request.POST["lname"]
		username = request.POST["username"]
		surveyor_id = request.POST["surveyor_id"]
		aadhaar_no = request.POST["aadhaar_no"]
		sex = request.POST["sex"]
		email = request.POST["email"]
		contact = request.POST["contact"]
		address = request.POST["address"]
		city = request.POST["city"]
		state = request.POST["state"]
		country = request.POST["country"]
		password = request.POST["password"]

		user = User.objects.create_user(username,email,password)
		user.first_name = fname
		user.last_name = lname
		user.save()

		if "photo" in request.FILES:
			photo = request.FILES["photo"]

		data = Surveyor(user=user,fname=fname,lname=lname,email=email,surveyor_id=surveyor_id,contact=contact,aadhaar_no=aadhaar_no,photo=photo,sex=sex,address=address,city=city,state=state,country=country)
		data.save()

		return render(request,'register_redirect.html')

	return render(request,'register.html')

def check_user(request):

	if request.method == "GET":
		username = request.GET["un"]
		check = User.objects.filter(username=username)

		if len(check) == 1:
			return HttpResponse("exists")
		else:
			return HttpResponse("not exists")

def aadhaar_authentication(request):

	if request.method == "GET":
		aadhaar_no = request.GET["adhar"]
		print(aadhaar_no)
		check = Aadhaar_data.objects.filter(aadhaar_no=aadhaar_no)
		if len(check) == 1:
			return HttpResponse("exists")
		else:
			return HttpResponse("not exists")


@csrf_exempt
def sms_response(request):

    # Use this data in your application logic
    from_number = request.form['From']
    body = request.form['Body']

    aadhaar_no_rec = int(body)

    data = Received_SMS(aadhaar_no = aadhaar_no_rec, mobile_no = from_number)
    data.save()

    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("Message Received")

    return HttpResponse(str(resp))

# Hindi

def index_hindi(request):

	if request.method == "POST":

		if 'login_form' in request.POST:

			username = request.POST["username"]
			password = request.POST["password"]

			user = authenticate(username=username, password=password)

			if user:
				login(request,user)
				return HttpResponseRedirect("/data_entry_page_hindi")
			else:
				return render(request,'index_hindi.html',{"status":"अमान्य उपयोगकर्ता नाम या पासवर्ड!"})

		if 'contact_form' in request.POST:

			fname = request.POST["fname"]
			lname = request.POST["lname"]
			state = request.POST["state"]
			email = request.POST["email"]
			subject = request.POST["subject"]

			data = Contact(fname=fname,lname=lname,state=state,email=email,subject=subject)
			data.save()

			return render(request,'contact_form_redirect_hindi.html')

		elif 'feedback_form' in request.POST:

			fname = request.POST["fname"]
			lname = request.POST["lname"]
			email = request.POST["email"]
			subject = request.POST["subject"]
			rating = request.POST["rating"]

			data = Feedback(fname=fname,lname=lname,email=email,subject=subject,rating=rating)
			data.save()

			return render(request,'feedback_form_redirect_hindi.html')

	return render(request,'index_hindi.html')

@login_required
def data_entry_hindi(request):

	surveyor_data = Surveyor.objects.get(user__id=request.user.id)
	context = {}
	context["surveyor_data"] = surveyor_data

	if 'data_entry_form' in request.POST:

		fname = request.POST["fname"]
		lname = request.POST["lname"]
		aadhaar_no = request.POST["aadhaar_no"]
		dob = request.POST["dob"]
		sex = request.POST["sex"]
		email = request.POST["email"]
		mobile_no = request.POST["mobile_no"]
		address = request.POST["address"]
		city = request.POST["city"]
		state = request.POST["state"]
		country = request.POST["country"]
		occupation = request.POST["occupation"]
		family_members = request.POST["family_members"]

		data = Civilian_data(fname=fname,lname=lname,aadhaar_no=aadhaar_no,dob=dob,sex=sex,email=email,mobile_no=mobile_no,address=address,city=city,state=state,country=country,occupation=occupation,family_members=family_members)
		data.save()

		return render(request,'data_entry_form_redirect_hindi.html')

	return render(request,'data_entry_hindi.html',context)

@login_required
def user_logout_hindi(request):
	logout(request)
	return HttpResponseRedirect("/homepage_hindi")

def register_hindi(request):

	if 'registration_form' in request.POST:
		fname = request.POST["fname"]
		lname = request.POST["lname"]
		username = request.POST["username"]
		surveyor_id = request.POST["surveyor_id"]
		aadhaar_no = request.POST["aadhaar_no"]
		sex = request.POST["sex"]
		email = request.POST["email"]
		contact = request.POST["contact"]
		address = request.POST["address"]
		city = request.POST["city"]
		state = request.POST["state"]
		country = request.POST["country"]
		password = request.POST["password"]

		user = User.objects.create_user(username,email,password)
		user.first_name = fname
		user.last_name = lname
		user.save()

		if "photo" in request.FILES:
			photo = request.FILES["photo"]

		data = Surveyor(user=user,fname=fname,lname=lname,email=email,surveyor_id=surveyor_id,contact=contact,aadhaar_no=aadhaar_no,photo=photo,sex=sex,address=address,city=city,state=state,country=country)
		data.save()

		return render(request,'register_redirect_hindi.html')

	return render(request,'register_hindi.html')