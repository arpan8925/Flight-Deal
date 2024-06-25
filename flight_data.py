

class FlightData:
    def __init__(self, flight_offer):
        self.price = flight_offer['price']['total']
        self.currency = flight_offer['price']['currency']
        self.departure_airport = flight_offer['itineraries'][0]['segments'][0]['departure']['iataCode']
        self.departure_time = flight_offer['itineraries'][0]['segments'][0]['departure']['at']
        self.arrival_airport = flight_offer['itineraries'][0]['segments'][0]['arrival']['iataCode']
        self.arrival_time = flight_offer['itineraries'][0]['segments'][0]['arrival']['at']
        self.carrier_code = flight_offer['itineraries'][0]['segments'][0]['carrierCode']
        self.carrier_numb = flight_offer['itineraries'][0]['segments'][0]['number']
        self.duration = flight_offer['itineraries'][0]['duration']
        self.segments = [{
            "departure_airport": segment['departure']['iataCode'],
            "departure_time": segment['departure']['at'],
            "arrival_airport": segment['arrival']['iataCode'],
            "arrival_time": segment['arrival']['at'],
            "carrier_code": segment['carrierCode'],
            "carrier_numb": segment['number'],
            "duration": segment['duration']
        } for segment in flight_offer['itineraries'][0]['segments']]
    
    def __str__(self):
        return f"Price: {self.price} {self.currency}, Departure: {self.departure_airport} at {self.departure_time}, Arrival: {self.arrival_airport} at {self.arrival_time}, Carrier: {self.carrier_code}{self.carrier_numb}, Duration: {self.duration}"
    
    def flight_current_price(self):
        return self.price
