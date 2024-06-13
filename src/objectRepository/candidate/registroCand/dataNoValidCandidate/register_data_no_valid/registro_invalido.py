from dotenv import dotenv_values
from src.objectRepository.candidate.registroCand.registerValid.stepRegisterCandidate import step_register_candidate
from src.services.catalogs import data_user
from src.services.peticiones_HTTP import send_post
env = dotenv_values("etc/.env")

name, last_name, second_last_name, birth_date, email_candidate = data_user(env)

data_payloads = [
    {
        "email": email_candidate,
        "keySystem": "MEX",
        "acceptPrivacy": False,
        "acceptTerms": False,
        "nationalityId": "undefined"
    },
    {
        "email": email_candidate,
        "keySystem": "MEX",
        "acceptPrivacy": True,
        "acceptTerms": False,
        "nationalityId": "undefined"
    },
    {
        "email": email_candidate,
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
        url = env["URL_SERVER"] + 'auth/registry/candidate'
        resultado = send_post(url, data, (400, 423))
        print(f"Resultado con datos: {data}, código: {code}")
        print('Se hicieron las pruebas de registro con datos no validos', resultado)
        return 'Se hicieron las pruebas de registro invalido'
    except Exception as e:
        print('No pasaron las pruebas de registro', e)
        return 'No pasaron las pruebas registro con datos incorrectos para el candidato'


def register_invalid_candidate():
    try:
        for data in data_payloads:
            register400_candidate(data.copy(), 400 if data["email"] else 409)
            print('\n')
        headers, email_candidate = step_register_candidate()
        print('Se hicieron las pruebas de registro para un usuario candidato con datos incorrectos')
        return 'Se hicieron las pruebas de registro para un usuario candidato con datos incorrectos', headers, email_candidate
    except Exception as e:
        print('No pasaron las pruebas de registro', e)
        return 'No pasaron las pruebas de registro con datos incorrectos'




