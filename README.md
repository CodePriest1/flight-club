# flight-club
You can start the application by running FlightClub "main.py"
Start By Making Your Own Copy Of The Google Sheet 
Make a copy of the google sheet using the link https://docs.google.com/spreadsheets/d/1YMK-kYDYwuiGZoawQy7zyDjEIU9u8oggCV4H2M9j7os/edit#gid=0

#...................................API REQUIRED.................................................#
Api required https://sheety.co/ (you will need to sign in with your google acccount, same one you will use to copy the data using the link in 4)
KIWI partners flight search Api https://partners.kiwi.com/ (free sign up)
Tequila Flight Search Api Documentation (https://tequila.kiwi.com/portal/login)
Twilio Sms Api https://www.twilio.com/docs/sms

#.................................PROGRAM REQUIREMENT.............................................#
Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air Transport Association (IATA) codes for each city. Most of the cities in the sheet include multiple airports, you want the city code.

Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.

If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number with the Twilio API.

The SMS should include the departure airport IATA code, destination airport IATA code, departure city, destination city, flight price and flight dates.e.g
![2020-07-30_10-15-26-8ea30ff9fc497564bddbee81e6f36da5](https://user-images.githubusercontent.com/88582897/174786945-b7622790-7e08-456b-a93a-382f23f755fb.png)


Enable the PUT option, so you can write to google sheet

Register with the Kiwi Partners Flight Search API
Your account name should be the same as what you used later in "First name" and "Last name".
There is no need to provide a credit card or billing information (you can skip that section) when you create your "Solution" (previously called "Application").
Go to MY SOLUTION by the left panel and then click on CREATE SOLUTION, then choose META SEARCH as your product type, then choose ONE-WAY RETURN, then create.
<img width="1213" alt="2021-01-29_16-19-23-a8c74121625c97789adc26f7bf985047" src="https://user-images.githubusercontent.com/88582897/174790116-57b4e2ad-5e54-4d9d-94c2-05e364b24570.png">

https://img-c.udemycdn.com/redactor/raw/article_lecture/2021-01-29_16-18-22-59e7a95f77f5964329d8e1037721ab3b.png


https://img-c.udemycdn.com/redactor/raw/article_lecture/2021-01-29_16-21-09-313d06d56e4eebcff7e01479b3d1f8d3.png

https://img-c.udemycdn.com/redactor/raw/article_lecture/2021-01-29_16-22-24-471f5e3dc034a1a10b79f9f6c1201792.png


data_manager.py is responsible for communicating with sheety
notification_manager.py is reponsible for communicating with Twilio
flight_search.py is responsible for interacting with Kiwi flight search to get IATACODE and get available flights
flight_data.py is responsible for structuring the flight data

