from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from bus.forms import UserForm

#REGISTRATION Process
def register(request):
	errors=""
	if request.method=='POST':
		form = UserForm(data=request.POST)
		if form.is_valid():
			user = form.save()
			user.set_password(user.password)
			user.save()
			return redirect("/")
		else:
			errors=form.errors	
	else:
		form=UserForm()
	return render(request,'bus/register.html',{'form':form,'errors':errors})		



def logout_view(request):
	logout(request)
	return redirect('/')



#Login Process
def login_view(request):
	errors =""
	if request.method == 'POST':
		data = request.POST
		username=data.get('username')
		password=data.get('password')
		user = authenticate(username=username,password=password)
		login(request=request,user=user)
		if user:
			return redirect('/')
		else:
			errors="Username password invalid"	
	
	return render(request,'bus/login.html',{'errors':errors})