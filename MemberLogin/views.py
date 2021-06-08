from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from Coordinator import views

# Create your views here.

def user_distribution(request,user):
    if user.user_type == 'Mentor':
        return redirect('coordinator:coordinterns')
    elif user.user_type == 'HR':
        return redirect('hr:hrintern')
    else:
        return redirect('')

def loginBasics(request):
    if request.user.is_authenticated:
        return user_distribution(request,request.user)
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user_type = request.POST['usertype']

        user = authenticate(request, username = email,password = password,user_type = user_type)
        if user is not None:
            login(request, user)
            return user_distribution(request, user)
        else:
            return render(request,'MemberLogin/loginbasic.html')
    else:
        return render(request,'MemberLogin/loginbasic.html')

