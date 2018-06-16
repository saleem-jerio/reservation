from hotel import Hotel 
from customer import Customer
from reservation import Reservation
#import notification



def list_resevrations_for_hotel(hotel_name):
				
	list_resevrations_for_hotel=[]			
	for reservation in Reservation.reservations:
		if reservation[0]==hotel_name:
			list_resevrations_for_hotel.append(reservation[1])
	return list_resevrations_for_hotel

def list_of_hotels_in_city(city):
	list_of_hotels_in_city=[]
	for hotel in Hotel.hotels:
		if city==hotel[2]:
			list_of_hotels_in_city.append( hotel[1]+' '+str(hotel[3])+ ' rooms, and '+str(hotel[4])+' are available')
	return list_of_hotels_in_city


			
###################################################
hiltonT=Hotel(4,'hiltonT','tripoli',100,10)

sheratonT=Hotel(4,'sheratonT','tripoli',40,1)

_4seasonT=Hotel(4,'4seasonT','tripoli',80,30)

hiltonD=Hotel(4,'hiltonD','dubai',100,10)

sheratonD=Hotel(4,'sheratonD','dubai',40,1)

_4seasonD=Hotel(4,'4seasonD','dubai',80,0)

##################################################
saleem=Customer('saleem','0927331257')


saleem=Customer('saleem','0927331257') 

ahmed=Customer('ahmed','0999999999')

##################################################
saleem=Reservation('hiltonD','dubai','saleem','0927331257')
 
salah=Reservation('hiltonT','tripoli','salah','0989898989')

#####################################################


		
