from django.conf.urls import url
from django.urls import path
from sankalan_app import views

# Template URLs
app_name = 'sankalan_app'

urlpatterns = [
	url(r'^$',views.index,name='index'),
]