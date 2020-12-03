import phonenumbers # import installed python package "phonenumbers"
from phone_numbers import myNumber # import a phone number you want to find
from phonenumbers import geocoder # geo location function from phonenumbers package
from phonenumbers import carrier # get the service provider of a number 

def get_user_country():
	try:
		location = phonenumbers.parse(myNumber, 'CH') # 'CH' means COUNTRY HISTORY
		if location:
			print('Your current country is ' + geocoder.description_for_number(location, "en"))
		else:
			print('Country not avaliable')
	except:
		print("Country not found!!")

def get_tel_provider():
	try:
		service_provider = phonenumbers.parse(myNumber, 'RO')
		if service_provider:
			print("Your service provider is " + carrier.name_for_number(service_provider, 'en'))
		else:
			print('Service provider not avaliable')
	except:
		print("Service provider not found!!")


get_user_country()
get_tel_provider()
