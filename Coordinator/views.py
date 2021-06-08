from django.conf.urls import url
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def Coordinator_Interns(request):
    return render(request,'Coordinator/co-ordinator-interns.html',{'user':request.user})


@login_required
def Coordinator_Review(request):
    return render(request,'Coordinator/co-ordinator-review.html',{'user':request.user})

@login_required
def Coordinator_Track(request):
    return render(request,'Coordinator/co-ordinator-track.html',{'user':request.user})