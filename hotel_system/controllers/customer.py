class Customer():
	customers=[]

	def __init__(self, name ,phone_number):

		self.customer_name=name
		self.customer_phone_number=phone_number
		
		#if [self.customer_name,self.customer_phone_number] in Customer.customers:
		#	print 'this customer already exist'

		if [self.customer_name,self.customer_phone_number] not in Customer.customers:
			Customer.customers.append([self.customer_name,self.customer_phone_number])
		#	print 'customer added succesfully'
			