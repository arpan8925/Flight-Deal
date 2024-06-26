from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager
import datetime

flight = FlightSearch()
data_manager = DataManager()
city_codes = data_manager.cities()
my_price = data_manager.flight_price()
email_notification = NotificationManager()

origin = "DAC"
departure_date = datetime.datetime(year=2024, month=8, day=2)

for destination in city_codes:
    flight_offers = flight.search_flight(origin=origin, departure_date=departure_date, destination=destination)

    if flight_offers:
        for offer in flight_offers["data"]:
            live_flight_info = FlightData(flight_offer = offer)

            if float(live_flight_info.flight_current_price()) < float(my_price[city_codes.index(destination)]):
                print(f"flight from {origin} to {destination}: {live_flight_info}")
                email_notification.notify(live_flight_info)
                
            else:
                print(f"No cheaper flight found for {destination}")

            break





