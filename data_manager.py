import requests

SHEET_PUT = "SHEET PUT"
SHEET_GET = "SHEET GET"
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    pass

    def get_sheet_data(self):
        response = requests.get(url=SHEET_GET)
        response.raise_for_status()
        data = response.json()
        self.sheet_data = data["prices"]
        return self.sheet_data

    def update_code(self):
        for row in self.sheet_data:
            new_data = {
                "price":
                    {"iataCode": row["iataCode"]}}

            response = requests.put(url=f"{SHEET_PUT}/{row['id']}", json=new_data)
            response.json()
        print(response.text)


