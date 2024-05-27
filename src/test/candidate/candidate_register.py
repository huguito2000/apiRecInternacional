import requests
import json
import random
from json import loads
from dotenv import dotenv_values
from src.services.catalogs import *

env = dotenv_values("etc/.env")

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json'
}

def get_profile(token):
    headers.update({'Authorization': token})
    response = requests.get(env["URL_SERVER"] + "user/candidate", headers=headers)
    json_dict = loads(response.text)
    return json_dict

def step_register(email, nationality_id):
    print("Registro de candidato")
    json_data = {
        'email': email,
        'keySystem': "MEX",
        'nationalityId': nationality_id,
        'acceptTerms': True,
        'acceptPrivacy': True
    }

    response = requests.post(
        env["URL_SERVER"] + "auth/registry/candidate", headers=headers, json=json_data)
    
    if(response.status_code == 201):
        token = response.headers['Token']
        print('Registro correcto')
    else:
        print(response.content)
        token = None
        print('Fallo el registro')
    return token

def step_verify_email(email, code):
    print("Verificacion de correo")
    response = requests.post(env["URL_SERVER"] + "auth/verify-email?email="+email+"&code=" +code, headers=headers)
    print(response.content)

def step_create_pass(token, password):
    print("Creacion de contraseña")
    headers.update({'Authorization': token})
    response = requests.put(env["URL_SERVER"] + "auth/create-pass?password=" + password, headers=headers)
    print(response.content)


def step_register_permissions(token):
    print("Registro de permisos")
    headers.update({'Authorization': token})

    json_data = [
        {'status': True, 'permissionType': 'NOTIFICATION_PROCESS'},
        {'status': True, 'permissionType': 'REMINDER'},
        {'status': True, 'permissionType': 'JOB_VACANCIES'},
        {'status': True, 'permissionType': 'NEWSLETTER_INTERNAL'},
        {'status': True, 'permissionType': 'NEWSLETTER_EXTERNAL'},
        {'status': True, 'permissionType': 'RECOMMENDATIONS'}
    ]

    response = requests.post(env["URL_SERVER"] + "user/permissions/register-list", headers=headers, json=json_data)
    print(response.content)

def step_register_phone(token):
    ("Registro de telefono")
    headers.update({'Authorization': token})
    response = requests.post(env["URL_SERVER"] + "auth/send-sms?phone=5555555550&phoneCode=%2B52", headers=headers)
    print(response.content)

def step_verify_phone(token):
    print("Verificacion de telefono")
    headers.update({'Authorization': token})
    response = requests.post(env["URL_SERVER"] + "auth/verify-code-sms?code=110901&phone=5555555550&phoneCode=%2B52", headers=headers)
    print(response.content)

def step_complete_profile(token, name, lastname, birth_date, area_id, city_id):
    print("Registro de datos finales")
    json_data = {
        'name': name,
        'lastName': lastname,
        'dateBirth': str(birth_date),
        'areaId': area_id,
        'cityId': city_id
    }

    headers.update({'Authorization': token})
    response = requests.post(env["URL_SERVER"] + "auth/registry/candidate/complete", headers=headers, json=json_data)
    print(response.content)


def register_candidate(name, lastname, email, password, birth_date):
    token = step_register(email, get_ramdom_nationality()["nationalityId"])
    if(token != None):
        candidate = get_profile(token)
        step_verify_email(email, candidate["user"]["checkCode"])
        step_create_pass(token, password)
        step_register_permissions(token)
        step_register_phone(token)
        step_verify_phone(token)
        step_complete_profile(token, name, lastname, birth_date, get_ramdom_area()["areaId"], get_ramdom_city()["cityId"])
    else:
        print("Se cancela el registro")


