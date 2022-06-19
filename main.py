#MAIN AIM; The aim of this code is to get a text whenever there's an available flight with a price lower than what we have in the sheets. In my case, my departure is LONDON. So i'm looking to get a flight that goes from LONDON to any of those cities in the sheets, but at a ticket price lower than the prices set in the sheet. We should get a text message when the flight tickets are lower than the ticket prices on the sheet.
#Make your copy of your own starting google sheet using the link https://docs.google.com/spreadsheets/d/1YMK-kYDYwuiGZoawQy7zyDjEIU9u8oggCV4H2M9j7os/edit#gid=0
#go to file and make a copy of the sheet
#Api required https://sheety.co/
#You will need to login to kiwi to get started and to get the kiwi Api using https://partners.kiwi.com/
#https://tequila.kiwi.com/portal/login to access the kiwi documentation
#I'm making use of Twilio to be able to send text automatically, use the link to create an account https://www.twilio.com/docs/sms
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
        #To get the IATACODE for each city my passing the city to Kiwi using the object fs from Class FlightSearch
        row["iataCode"] = fs.get_location_data(row["city"])
    print(sheet_data)
    data_manager.sheet_data = sheet_data #new sheet data with IATACODES
    data_manager.update_code() #This passes the actual IATACODES to sheety
for destination in sheet_data:
#We need to check is there is any available flight that goes from LONDON to any of the cities in our sheet by passing it to the Class FlightSearch passing in our ORIGIN IATA CODE and each of the cities in our sheet, also passing tomorrow's date and date in 6 months from now
    flight = fs.check_flight(ORIGIN_IATA_CODE,
                             destination["iataCode"],
                             tomorrows_date.strftime("%d/%m/%Y"),
                             six_months_from_today.strftime("%d/%m/%Y"))
    if flight.price < destination["lowestPrice"]:

        nm.send_message(f"Low price alert! Only £{flight.price} to travel from "
                        f"{flight.departure_city}--{flight.departure_airport} to "
                        f"{flight.destination_city}-{flight.destination_airport}, "
                        f"from {flight.departure_date} to {flight.arrival_date}.")
