from flight_search import FlightSearch
from flight_data import FlightData
import datetime

flight = FlightSearch()

origin = "DEL"
destination = "DAC"
departure_date = datetime.datetime(year=2024, month=8, day=2)

# Search for flights
flight_offers = flight.search_flight(origin=origin, destination=destination, departure_date=departure_date)

# Organize the flight data
if flight_offers:
    for offer in flight_offers["data"]:
        flight_data = FlightData(offer)
        print(flight_data)
