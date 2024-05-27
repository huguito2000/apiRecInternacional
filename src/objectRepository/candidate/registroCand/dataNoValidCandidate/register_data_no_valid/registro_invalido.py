from datetime import datetime

from src.objectRepository.candidate.registroCand.registerValid.stepRegisterCandidate import step_register_candidate
from src.services.funciones import base, send_post
def email_new():
    now = datetime.now()
    correo = 'cand' + str(now.day) + str(now.month) + str(now.minute) + str(now.second) + '@yopmail.com'
    return correo

correo = email_new()

data_payloads = [
    {
        "email": correo,
        "keySystem": "MEX",
        "acceptPrivacy": False,
        "acceptTerms": False,
        "nationalityId": "undefined"
    },
    {
        "email": correo,
        "keySystem": "MEX",
        "acceptPrivacy": True,
        "acceptTerms": False,
        "nationalityId": "undefined"
    },
    {
        "email": correo,
        "keySystem": "MEX",
        "acceptPrivacy": False,
        "acceptTerms": True,
        "nationalityId": "undefined"
    },
    {
        "email": "@yopmail.com",
        "keySystem": "MEX",
        "acceptPrivacy": True,
        "acceptTerms": True,
        "nationalityId": "undefined"
    },
    {
        "email": "2903",
        "keySystem": "MEX",
        "acceptPrivacy": True,
        "acceptTerms": True,
        "nationalityId": "undefined"
    },
    {
        "email": "2903yopmail.com",
        "keySystem": "MEX",
        "acceptPrivacy": True,
        "acceptTerms": True,
        "nationalityId": "undefined"
    },
    {
        "email": "",
        "keySystem": "MEX",
        "acceptPrivacy": True,
        "acceptTerms": True,
        "nationalityId": "undefined"
    },

    {
        "email": "1705qa@yopmail.com",
        "keySystem": "ESP",
        "acceptPrivacy": True,
        "acceptTerms": True,
        "nationalityId": "40288086796ba27001796bbd39f70038"
    },
]

def register400_candidate(data, code):
    try:
        url = base + 'auth/registry/candidate'
        resultado = send_post(url, data, code)
        print(f"Resultado con datos: {data}, código: {code}")
        print('Se hicieron las preubas de registro invalido', resultado)
        return 'Se hicieron las pruebas de registro invalido'
    except Exception as e:
        print(e)
        return 'No se hizo las pruebas correctamente'


def register_invalid_candidate():
    try:
        for data in data_payloads:
            register400_candidate(data.copy(), 400 if data["email"] else 409)  # Use copy() to avoid modifying original data
        headers, correo = step_register_candidate()
        print('Se hicieron las pruebas de login invalido')
        return 'Se hicieron las pruebas de login', headers, correo
    except Exception as e:
        print('no se hicieron las pruebas de login', e)
        return 'no se hicieron las pruebas de login'



