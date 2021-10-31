"""Testing web APIs with HTTP GET method"""

import json
import sys

import requests

def print_coord(address):
    """Retrieve coordinates from Open Street Map"""
    osm = "https://nominatim.openstreetmap.org/search"
    data = {'q': address, 'format': 'json'}
    resp = requests.get(osm, data)
    json_list = json.loads(resp.text)
    for item in json_list:
        display_name = item['display_name']
        short_name = display_name.split(", ")[0]
        lat = item['lat']
        lon = item['lon']
        print(f"{short_name} ({lat} - {lon})")

def print_info(country_name):
    """Retrieve country info from REST API"""
    base_url = "http://restcountries.com/v3.1/"
    name_url = base_url + "name/"
    code_url = base_url + "alpha/"
    resp = requests.get(name_url + country_name)
    try:
        country = resp.json()[0]
        languages = country['languages']
        print(f"Languages: {', '.join(languages.values())}")
        border_codes = country['borders']
        border_names = []
        for code in border_codes:
            resp = requests.get(code_url + code)
            border_country = resp.json()[0]
            border_name = border_country["name"]["common"]
            border_names.append(border_name)
        print(f"Borders: {', '.join(border_names)}")
    except KeyError:
        print("Unknown country, please use English or native name")

if __name__ == "__main__":
    try:
        service = sys.argv[1]
        if service == "coord":
            try:
                my_address = sys.argv[2]
                print_coord(my_address)
            except IndexError:
                print("Please enter an address")
        elif service == "info":
            try:
                my_country_name = sys.argv[2]
                print_info(my_country_name)
            except IndexError:
                print("Please enter a country name")
        else:
            print("Unknown action, please use either 'coord' or 'info'")
    except IndexError:
        print("Missing action, please use either 'coord' or 'info'")
