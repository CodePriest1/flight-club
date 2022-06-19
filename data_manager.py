import requests

SHEET_PUT = "SHEET PUT"
SHEET_GET = "SHEET GET"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    pass
    
    # This is to get the data in the sheet from sheety
    def get_sheet_data(self):
        response = requests.get(url=SHEET_GET)
        response.raise_for_status()
        data = response.json()
        self.sheet_data = data["prices"]
        return self.sheet_data

    #This is to pass the IATACODE to the sheet in sheety using the PUT for each of the countries
    def update_code(self):
        for row in self.sheet_data:
            new_data = {
                "price":
                    {"iataCode": row["iataCode"]}}

            response = requests.put(url=f"{SHEET_PUT}/{row['id']}", json=new_data)
            response.json()
        print(response.text)


