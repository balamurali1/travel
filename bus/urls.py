from django.urls import path
from django.views.generic.base import TemplateView 
from django.contrib.auth.models import User


from bus.models import Car
from bus.models import Passenger
from bus.models import Trip


from bus.views import car_create,car_update,car_delete,home1,home2,home3,passenger_create,passenger_update,passenger_delete,trip_create,trip_update,trip_delete,user_create,user_update,user_delete

urlpatterns = [ 
    ##############User URLS################
    path('user1/',TemplateView.as_view(template_name = 'bus/user1.html',
      extra_context={'data':User.objects.all()}
      )),
    path("user_create/",user_create),
    path("user_update/<int:pk>/",user_update),
    path("user_delete/<int:pk>/",user_delete),


    #############Car URL#############
     path('car1/',home1),
    # path('car1/',TemplateView.as_view(template_name="bus/home1.html",
    #   extra_context={"data":Car.objects.all()}
    #   )),

    path("car_create/",car_create),
    path("car_update/<int:pk>/",car_update),
    path("car_delete/<int:pk>/",car_delete),

   ##############passenger URL#############
   path('passenger1/',home2),

   # path('passenger1/',TemplateView.as_view(template_name="bus/home2.html",
   #   extra_context={"data":Passenger.objects.all()}
   #  )),
   
   path("passenger_create/",passenger_create),
   path("passenger_update/<int:pk>/",passenger_update),
   path("passenger_delete/<int:pk>/",passenger_delete),



    ################Trip URL################
   path('trip1/',home3),
   # path('trip1/',TemplateView.as_view(template_name="bus/home3.html",
   #  extra_context={"data":Trip.objects.all()}
   #  )),

   path("trip_create/",trip_create),
   path("trip_update/<int:pk>/",trip_update),
   path("trip_delete/<int:pk>/",trip_delete),




]
