from flight_search import FlightSearch
from data_manager import DataManager
from datetime import datetime, timedelta
from notification_manager import NotificationManager

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


data_manager = DataManager()
sheet_data = data_manager.get_sheet_data()
fs = FlightSearch()
nm = NotificationManager()
# print(data.get_sheet_data())
ORIGIN_IATA_CODE = "LON"
today = datetime.now()
tomorrows_date = today + timedelta(days=1)
six_months_from_today = today + timedelta(days=6 * 30)

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = fs.get_location_data(row["city"])
    print(sheet_data)
    # data_manager.sheet_data = sheet_data
    data_manager.update_code()
for destination in sheet_data:
    flight = fs.check_flight(ORIGIN_IATA_CODE,
                             destination["iataCode"],
                             tomorrows_date.strftime("%d/%m/%Y"),
                             six_months_from_today.strftime("%d/%m/%Y"))
    if flight.price < destination["lowestPrice"]:

        nm.send_message(f"Low price alert! Only £{flight.price} to travel from "
                        f"{flight.departure_city}--{flight.departure_airport} to "
                        f"{flight.destination_city}-{flight.destination_airport}, "
                        f"from {flight.departure_date} to {flight.arrival_date}.")
