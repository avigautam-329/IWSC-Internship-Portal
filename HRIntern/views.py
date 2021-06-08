from django.conf.urls import url
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def HR_Intern(request):
    return render(request,'HRIntern/hr-intern.html',{'user':request.user})

@login_required
def HR_Review(request):
    return render(request,'HRIntern/hr-review.html',{'user':request.user})

@login_required
def HR_Track(request):
    return render(request,'HRIntern/hr-track.html',{'user':request.user})