import requests
import os
import dotenv

dotenv.load_dotenv()

class FlightSearch:
    def __init__(self):
        super().__init__()
     
        self.access_token = self.get_access_token()
        self.amadeus_flight_search_end = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        self.amadeus_header = {
            "Authorization": f"Bearer {self.access_token}"
        }


    def search_flight(self, departure_date, origin, destination, adults=1, currency="INR", travel_class="ECONOMY", stopage=False):
        
        self.amadeus_search_parameters = {
            "originLocationCode": origin,
            "destinationLocationCode": destination,
            "departureDate": departure_date.strftime("%Y-%m-%d"),
            "adults": adults,
            "currencyCode": currency,
            "travelClass": travel_class,
            "nonStop": str(stopage).lower()
        }
        
        try:
            response = requests.get(url=self.amadeus_flight_search_end, params=self.amadeus_search_parameters, headers=self.amadeus_header)
            response.raise_for_status()
            flight_offers = response.json()
            if flight_offers:
                return flight_offers
            else:
                print("No Flight Found.")
                return None
            
        except requests.exceptions.RequestException as e:
            print(f"An Error Occured {e}")
            return None



    def get_access_token(self):

        url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "grant_type": "client_credentials",
            "client_id": os.getenv("API_KEY"),
            "client_secret": os.getenv("API_SECRET")
        }
        try:          
            self.response = requests.post(url, headers=headers, data=data)
            self.response.raise_for_status()
            return self.response.json()['access_token']
        
        except requests.exceptions.RequestException as e:
            print(f"An Error Occured {e}")
            return None