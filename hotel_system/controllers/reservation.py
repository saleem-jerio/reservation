from hotel import Hotel
import customer
import notification

class Reservation():
	reservations=[]

	def get_all_reservations():
    		return reservations
			
	def __init__(self, hotel_name,city,customer_name,customer_phone_number):

		self.hotel_name=hotel_name
		self.customer_name=customer_name
		self.customer_phone_number=customer_phone_number
		
		customer.Customer(self.customer_name,self.customer_phone_number)
		for hotel in Hotel.hotels:
			if hotel_name==hotel[1] and city==hotel[2] and hotel[4]!=0:
				hotel[4]-=1
				Reservation.reservations.append([hotel_name,customer_name]) 
				#notification.Confirmation('Mr '+customer_name+', your room reserved successfully',customer_phone_number)




			