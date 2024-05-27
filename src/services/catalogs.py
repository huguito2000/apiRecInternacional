import requests
import json
import random
from json import loads
from dotenv import dotenv_values

env = dotenv_values("etc/.env")

def get_ramdom_area():
    response = requests.get(env["URL_SERVER"] + "management/catalog/area")
    json_dict = loads(response.text)
    area = json_dict[random.randint(0, len(json_dict)-1)]
    return area

def get_area(area_id):
    response = requests.get(env["URL_SERVER"] + "management/catalog/area")
    areas = loads(response.text)
    for area_tmp in areas:
        if area_tmp["areaId"] == area_id:
           areas

    return speciality["specialtyId"]

def get_ramdom_nationality():
    response = requests.get(env["URL_SERVER"] + "management/catalog/nationality")
    json_dict = loads(response.text)
    nationality = json_dict[random.randint(0, len(json_dict)-1)]
    return nationality

def get_ramdom_city():
    '''
    response = requests.get(env["URL_SERVER"] + "management/catalog/country")
    json_dict = loads(response.text)
    country = json_dict[random.randint(0, len(json_dict))]

    response = requests.get(env["URL_SERVER"] + "management/catalog/state?countryCode=" + country["iso2"])
    json_dict = loads(response.text)
    state = json_dict[random.randint(0, len(json_dict))]
    '''
    
    response = requests.get(env["URL_SERVER"] + "management/catalog/city?countryCode=MX&stateCode=MX-AGU")
    json_dict = loads(response.text)
    city = json_dict[random.randint(0, len(json_dict)-1)]
    return city