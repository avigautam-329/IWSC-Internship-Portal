from IWportal.HRIntern.views import HR_Intern, HR_Review
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from HRIntern import views

urlpatterns = [
    url(r"Intern/$",views.HR_Intern,name='hrintern'),
    url(r"Review/$",views.HR_Review,name='hrreview'),
    url(r"Track/$",views.HR_Track,name='hrtrack'),
]
