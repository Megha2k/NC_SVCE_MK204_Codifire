"""sankalan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from sankalan_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name="index"),
    url(r'^sankalan_app/',include('sankalan_app.urls')),
    url(r'^sms/',views.sms_response,name='sms'),
    path('homepage', views.index),
    path('data_entry_page', views.data_entry,name="data_entry"),
    path('register/', views.register),
    path('check_user/', views.check_user, name="check_user"),
    path('aadhaar_authentication/', views.aadhaar_authentication, name="aadhaar_authentication"),
    path('user_logout/', views.user_logout, name="user_logout"),

    # Hindi
    path('hindi', views.index_hindi),
    path('homepage_hindi', views.index_hindi,name="homepage_hindi"),
    path('data_entry_page_hindi', views.data_entry_hindi,name="data_entry_hindi"),
    path('register_hindi/', views.register_hindi),
    path('user_logout_hindi/', views.user_logout_hindi, name="user_logout_hindi"),
    
 ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)