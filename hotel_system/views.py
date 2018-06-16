
from controllers.hotel import *
from controllers.customer import *
from controllers.reservation import *
from controllers.notification import *
from controllers.main import *
from controllers.tester import *

from django.http import HttpResponse

    
def HotelList(request):
    # call the functions to fill all the data about hotels, customers, and reservations
    
    hotel_list =Hotel.hotels 

    hotel_list_output = "<ul>"
    for h in hotel_list:
        hotel_list_output += "<li>" + h[1] + "</li>"
    hotel_list_output += "</ul>"
    return HttpResponse(hotel_list_output)

def HotelInCity(request):
    # call the functions to fill all the data about hotels, customers, and reservations

    hotel_list =tester.list_of_hotels_in_city('tripoli')

    hotel_list_output = "<ul>"
    for h in hotel_list:
        hotel_list_output += "<li>" + h + "</li>"
    hotel_list_output += "</ul>"
    return HttpResponse(hotel_list_output)

def ReservationList(request):
    # call the functions to fill all the data about hotels, customers, and reservations
    reservation_list =Reservation.reservations 

    reservation_list_output = "<ul>"
    for h in reservation_list:
        reservation_list_output += "<li>" + h[0] +'>>>>>>>'+h[1]+ "</li>"
    reservation_list_output += "</ul>"
    return HttpResponse(reservation_list_output)
    