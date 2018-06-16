class Hotel():
	hotels=[]
		
	def __init__(self, number,name,city,total_rooms,available_rooms):

		self.hotel_number=number
		self.hotel_name=name
		self.city=city
		self.total_rooms=total_rooms
		self.available_rooms=available_rooms
		
		if [self.hotel_number,self.hotel_name,self.city,total_rooms,self.available_rooms] not in Hotel.hotels:

			Hotel.hotels.append([self.hotel_number,self.hotel_name,self.city,total_rooms,self.available_rooms])
			#print self.hotel_name+' '+'hotel added successfully'

		#else:
		#	return 'this hotel is already exist'

