from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from bus.models import Car
from bus.models import Passenger
from bus.models import Trip

from bus.forms import VehicleForm
from bus.forms import PassengerForm
from bus.forms import TripForm

from django.contrib.auth.models import User
from bus.forms import UserForm


# Create your views here.
##################User Information######################		

#User Create process
def user_create(request):
	message = ""
	if request.method == 'POST':
		form = UserForm(data = request.POST)
		if form.is_valid():
			form.save()
			return redirect("/users/user1/")
		else:
			message = form.errors

	else:
		form = UserForm()	
		
	return render(request,'bus/create4.html',{'msg':message,'form':form})

#User Update Process
def user_update(request,pk):
	if request.method == 'POST':
		user_obj = User.objects.get(id=pk)
		form = UserForm(request.POST,instance =user_obj)
		if form.is_valid():
			form.save()
			return redirect("/users/user1/")
	else:
		user_obj =User.objects.get(id=pk)
		form = UserForm(instance =user_obj)

	return render(request,'bus/update4.html',{'form':form})

#User Delete Process
def user_delete(request,pk):
	user_obj = User.objects.get(id=pk)
	if request.method == "POST":
		if "YES" in request.POST:
			user_obj.delete()
		return redirect("/users/user1/")

	else:
		return render(request,'bus/delete4.html',{'user':user_obj})


 
###########################Car Information###############
#@login_required
def home1(request):
	car_data = Car.objects.all()
	return render(request,'bus/home1.html',{'data':car_data})

#Create Process
def car_create(request):
	message = ""
	if request.method == 'POST':
		form = VehicleForm(data = request.POST)
		if form.is_valid():
			form.save()
			return redirect("/car/car1/")
		else:
			message = form.errors

	else:
		form = VehicleForm()	
		
	return render(request,'bus/create1.html',{'msg':message,'form':form})


#UPDATAE PROCESS
def car_update(request,pk):
	if request.method == 'POST':
		car_obj = Car.objects.get(id=pk)
		form = VehicleForm(request.POST,instance =car_obj)
		if form.is_valid():
			form.save()
			return redirect("/car/car1/")
	else:
		car_obj =Car.objects.get(id=pk)
		form = VehicleForm(instance =car_obj)

	return render(request,'bus/update1.html',{'form':form})	


#DELETE PROCESS is Optional Process
def car_delete(request,pk):
	car_obj = Car.objects.get(id=pk)
	if request.method == "POST":
		if "YES" in request.POST:
			car_obj.delete()
		return redirect("/car/car1/")

	else:
		return render(request,'bus/delete1.html',{'car':car_obj})

#############################Passenger information###########

@login_required
def home2(request):
	passenger_data = Passenger.objects.all()
	return render(request,'bus/home2.html',{'data':passenger_data})


#Create Process
def passenger_create(request):
	message = ""
	if request.method == 'POST':
		form = PassengerForm(data = request.POST)
		if form.is_valid():
			form.save()
			return redirect("/passenger/passenger1/")
		else:
			message = form.errors
	else:
		form = PassengerForm()	
		
	return render(request,'bus/create2.html',{'msg':message,'form':form})
	

#UPDATAE PROCESS

def passenger_update(request,pk):
	if request.method == 'POST':
		passenger_obj = Passenger.objects.get(id=pk)
		form = PassengerForm(request.POST,instance =passenger_obj)
		if form.is_valid():
			form.save()
			return redirect("/passenger/passenger1/")
	else:
		passenger_obj = Passenger.objects.get(id=pk)
		form = PassengerForm(instance =passenger_obj)

	return render(request,'bus/update2.html',{'form':form})


#DELETE PROCESS is Optional Process
def passenger_delete(request,pk):
	passenger_obj = Passenger.objects.get(id = pk)
	if request.method == "POST":
		if "YES" in request.POST:
			passenger_obj.delete()
		return redirect("/passenger/passenger1/")

	else:
		return render(request,'bus/delete2.html',{'passenger':passenger_obj})

####################Trip information##############
@login_required
def home3(request):
	trip_data = Trip.objects.all()
	return render(request,'bus/home3.html',{'data':trip_data})

#Create Process
def trip_create(request):
	message = ""
	if request.method == 'POST':
		form = TripForm(data = request.POST)
		if form.is_valid():
			form.save()
			return redirect("/trip/trip1/")
		else:
			message = form.errors
	else:
		form = TripForm()	
		
	return render(request,'bus/create3.html',{'msg':message,'form':form})
	


def trip_update(request,pk):
	if request.method == 'POST':
		trip_obj = Trip.objects.get(id=pk)
		form = TripForm(request.POST,instance =trip_obj)
		if form.is_valid():
			form.save()
			return redirect("/trip/trip1/")
	else:
		trip_obj = Trip.objects.get(id=pk)
		form = TripForm(instance =trip_obj)

	return render(request,'bus/update3.html',{'form':form})


#DELETE PROCESS is Optional Process
def trip_delete(request,pk):
	trip_obj = Trip.objects.get(id = pk)
	if request.method == "POST":
		if "YES" in request.POST:
			trip_obj.delete()
		return redirect("/passenger/passenger1/")

	else:
		return render(request,'bus/delete3.html',{'trip':trip_obj})
