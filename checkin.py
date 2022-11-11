from amadeus import Client, ResponseError

amadeus = Client()

try:
    response = amadeus.reference_data.urls.checkin_links.get(airlineCode='IB')
    print(response.data)
except ResponseError as error:
    print(error)
