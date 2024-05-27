import json
import string
import random
import secrets
from datetime import date, timedelta
from src.services.catalogs import *
from src.test.candidate.candidate_register import *
from src.test.candidate.candidate_postulation import *


def main(enviroment):
    with open(enviroment["RESOURCES_DIR"]+"data.json", "r", encoding="utf-8") as jsonFile:
        json_data = json.load(jsonFile)

        for x in range(1):
            gender = "M" if x % 2 == 0 else "F"

            name = get_ramdom_name(json_data, gender)
            last_name = get_ramdom_last_name(json_data)
            second_last_name = get_ramdom_last_name(json_data)
            birth_date = getbirth_date(True)
            email = get_email_by_name(name, last_name, second_last_name, birth_date)
            password = get_password(name, last_name, second_last_name, birth_date)
            register_candidate(name, last_name, email, password, birth_date)
            print("Se creo un nuevo usuario, accesos:")
            print("Email: " + email)
            print("Pass: " + password)


def get_ramdom_name(json_data, gender):
    key_map = ("namesM", "namesF")[gender == "M"]
    return (json_data[key_map][random.randint(0, len(json_data[key_map]) - 1)]).capitalize()


def get_ramdom_last_name(json_data):
    return (json_data["lastNames"][random.randint(0, len(json_data["lastNames"]) - 1)]).capitalize()


def getbirth_date(is_valid):
    date_start = date(1990, 1, 1)
    date_end = date(2005, 12, 31)

    if (not is_valid):
        date_start = date(2018, 1, 1)
        date_end = date(2023, 12, 31)

    randay = random.randrange((date_end - date_start).days)
    return date_start + timedelta(days=randay)


def get_email_by_name(name, last_name, second_last_name, birth_date: date):
    return normalize((name[0:2] + last_name[0:2] + second_last_name + "." + str(birth_date.year) + "@yopmail.com").lower())


def get_password(name, last_name, second_last_name, birth_date: date):
    return (name[0:2] + last_name[0:2] + second_last_name + "" + str(birth_date.year) + ".").capitalize()

def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ñ", "n"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s