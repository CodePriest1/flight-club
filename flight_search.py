import requests
from flight_data import FlightData
FLIGHT_SEARCH_API = "FLIGHT SEARCH API"
SEARCH_KEY = "SEARCH KEY"

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    pass
    
    #This function is to get the IATACODE by passing each city from our sheet to Kiwi. It returns the IATACODE whch we pass to the sheets using the Class Data_Manager
    def get_location_data(self, city):
        header = {"apikey": SEARCH_KEY}
        query = {"term": city, "location_types": "city"}
        location_api = f"{FLIGHT_SEARCH_API}/locations/query"
        response = requests.get(url=location_api, params=query, headers=header)
        response.raise_for_status()
        code = response.json()["locations"][0]["code"]
        return code

    def check_flight(self, fly_from, fly_to, date_from, date_to):
        header = {"apikey": SEARCH_KEY}
        search_api = f"{FLIGHT_SEARCH_API}/v2/search"
        query = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "curr": "GBP"
        }
        response = requests.get(url=search_api, params=query, headers=header)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {fly_to}.")
            return None

        flight_data = FlightData(
            price = data["price"],
            origin_city = data["route"][0]["cityFrom"],
            origin_airport = data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data

