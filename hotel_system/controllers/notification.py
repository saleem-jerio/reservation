'''from twilio.rest import Client

class Confirmation():
	def __init__(self, confimation,phone_number):
					
		# Your Account SID from twilio.com/console
		account_sid = "AC9fb47ec9d087b1efe33b0a03db71c483"
		# Your Auth Token from twilio.com/console
		auth_token  = "42e9a94c085d398025549d0bf4487ea2"

		client = Client(account_sid, auth_token)

		message = client.messages.create(
		    to=phone_number, 
		    from_="+14787969166",
		    body=confimation)

		print message.sid
'''