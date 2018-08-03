from django.shortcuts import render,redirect
from django.http import HttpResponse
from.import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
# signup------------
def signup_view(request):
  if request.method=='POST':
      form = RegistrationForm(request.POST)
      if form.is_valid():
  	    user=form.save()
  	    login(request,user)
  	    return redirect('accounts:profile')
  else:
	  form=RegistrationForm()

  return render(request,'accounts/signup.html',{'form':form})



#login--------------- 

def login_view(request):
  if request.method=='POST':
    form=AuthenticationForm(data=request.POST) 
    if form.is_valid():
      user=form.get_user()
      login(request,user)
      if'next'in request.POST:
        return redirect(request.POST.get('next'))
      else:
        return redirect('accounts:profile')
  else:
    form=AuthenticationForm()
  return render(request,'classroom/discussion.html',{'form':form})

#logout------------------

def logout_view(request):
  if request.method=='POST':
  	logout(request)
  	return redirect('accounts:login')

 

#profile
@login_required
def profile(request):
  user=request.user
  return render(request,'accounts/profile.html',{'user':user})