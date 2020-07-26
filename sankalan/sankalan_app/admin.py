from django.contrib import admin
from sankalan_app.models import Contact
from sankalan_app.models import Feedback
from sankalan_app.models import Civilian_data
from sankalan_app.models import Surveyor

# Register your models here.
# This is just a comment
admin.site.site_header = "SANKALAN Administration"

class ContactAdmin(admin.ModelAdmin):
	list_display = ["fname","lname","state"]
	search_fields = ["fname","lname","email","state"]
	readonly_fields = ["fname","lname","email","state","subject"]
	list_filter = ['state']

class FeedbackAdmin(admin.ModelAdmin):
	list_display = ["fname","lname","rating"]
	search_fields = ["fname","lname","state","rating"]
	readonly_fields = ["fname","lname","email","rating","subject"]
	list_filter = ['rating']

class Civilian_dataAdmin(admin.ModelAdmin):
	list_display = ["fname","lname","aadhaar_no","state","date"]
	search_fields = ["fname","lname","email","aadhaar_no","mobile_no","city","state","occupation","date"]
	readonly_fields = ["date"]
	list_filter = ['state','city']

class SurveyorAdmin(admin.ModelAdmin):
	list_display = ["fname","lname","surveyor_id","state"]
	search_fields = ["fname","lname","email","state","surveyor_id","aadhaar_no","city","state"]
	list_filter = ['state','city']

admin.site.register(Contact,ContactAdmin)
admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(Civilian_data,Civilian_dataAdmin)
admin.site.register(Surveyor,SurveyorAdmin)