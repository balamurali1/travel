"""travel URL Configuration 

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from bus.views import primary
from django.views.generic.base import TemplateView
from bus.user_views import register,login_view,logout_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path("",TemplateView.as_view(template_name="bus/primary.html")),

    path("car/",include("bus.urls")),

    path("passenger/",include("bus.urls")),

    path("trip/",include("bus.urls")),

    path("register/",register),

    path("login/",login_view),
    path('logout/',logout_view),

    path('users/',include('bus.urls')),


]

