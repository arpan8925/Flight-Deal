class FlightSearch:
    pass


import requests
import datetime
import json

API_KEY = '1FTyGNf96GOhUIDxSa51OikyGGxyeXpT'
API_SECRET = 'eOgrteOl6l0gX4G7'

# Function to get access token
def get_access_token():
    url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": API_KEY,
        "client_secret": API_SECRET
    }
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()  # Ensure we catch errors
    return response.json()['access_token']


ACCESS_TOKEN = get_access_token()

amadeus_flight_search_end = "https://test.api.amadeus.com/v2/shopping/flight-offers"

amadeus_header = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

date = datetime.datetime(year=2024, month=8, day=2)

amadeus_search_parameters = {
    "originLocationCode": "DAC",
    "destinationLocationCode": "SHA",
    "departureDate": date.strftime("%Y-%m-%d"),
    "adults": 1,
    "currencyCode": "INR",
    "travelClass": "ECONOMY"
}

response = requests.get(url=amadeus_flight_search_end, params=amadeus_search_parameters, headers=amadeus_header)
response.raise_for_status() 

# Print the response data
flight_offers = response.json()["data"][0]
print(flight_offers["travelerPricings"][0]["price"])

