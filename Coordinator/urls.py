from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from Coordinator import views

app_name = 'Coordinator'

urlpatterns = [
    url(r"Interns/$",views.Coordinator_Interns,name='coordinterns'),
    url(r"Review/$",views.Coordinator_Review,name='coordreview'),
    url(r"Track/$",views.Coordinator_Track,name='coordtrack'),
]