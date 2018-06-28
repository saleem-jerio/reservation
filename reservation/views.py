# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from models import *

# Create your views here.

def AllHotels(request):
    all_hotels = "<ul>"
    for hotel in Hotel.objects.all():
        all_hotels = all_hotels + "<li>" + hotel.hotel_name + "</li>"
        all_hotels += "</ul>"

    return HttpResponse(all_hotels)

def AllCustomers(request):
    all_customers = "<ul>"
    for customer in Customer.objects.all():
        all_customers = all_customers + "<li>" + customer.customer_name + "</li>"
        all_customers += "</ul>"

    return HttpResponse(all_customers)

def AllReservations(request):
    all_reservations = "<ul>"
    for reservation in Reservation.objects.all():
        all_reservations = all_reservations + "<li>"+reservation.hotel.hotel_name + ' ' + reservation.customer.customer_name +"</li>"
        all_reservations += "</ul>"

    return HttpResponse(all_reservations)