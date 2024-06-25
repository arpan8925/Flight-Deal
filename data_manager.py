import requests

class DataManager:
    def __init__(self):
        self.sheety_end = "https://api.sheety.co/7dd323f370a1fa5581a130fb15e4a412/flightDeals/prices"
        self.sheet = self.my_sheet()
        self.city_codes = self.get_city_codes()
        self.lowest_price = self.get_prices()

    def my_sheet(self):
        response = requests.get(url=self.sheety_end)
        return response.json()["prices"]

    def get_city_codes(self):
        return [city["iataCode"] for city in self.sheet]

    def cities(self):
        return self.city_codes
    
    def get_prices(self):
        return [price["lowestPrice"] for price in self.sheet]
    
    def flight_price(self):
        return self.lowest_price


