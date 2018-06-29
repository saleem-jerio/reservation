# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from models import *

# Create your views here.

def AllHotels(request):

    return render(request,"reservation/hotels.html",
                    {"hotels":Hotel.objects.all()})

def AllCustomers(request):

    return render(request,"reservation/customers.html",
                {"customers":Customer.objects.all()})

def AllReservations(request):

    return render(request,"reservation/reservation.html",
                {"reservations":Reservation.objects.all()})