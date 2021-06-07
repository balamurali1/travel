from django import forms
from bus.models import Car
from bus.models import Passenger 
from bus.models import Trip
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','password'] 

######Car Form##############
class VehicleForm(forms.ModelForm):
	class Meta:
		model = Car
		fields = "__all__"
		#fields = ['name','number']
		#exclude=['fair']


##########Passenger Form##############
class PassengerForm(forms.ModelForm):
	class Meta:
		model = Passenger
		fields = "__all__"

##########Trip Form#########

class TripForm(forms.ModelForm):
	class Meta:
		model = Trip
		fields = "__all__"




