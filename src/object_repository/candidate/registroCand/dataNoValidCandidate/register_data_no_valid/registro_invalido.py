from src.objectRepository.candidate.registroCand.registerValid.stepRegisterCandidate import step_register_candidate
from src.services.catalogs import data_user, env
from src.services.peticiones_HTTP import send_post


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
        if resultado != 0:
            print(f"Resultado con datos: {data}, código: {code}")
            print('Se hicieron las pruebas de registro con datos no validos\n', resultado)
            return 'Se hicieron las pruebas de registro invalido', 1
        else:
            print('No pasaron las pruebas de registro\n')
            return 'No pasaron las pruebas registro con datos incorrectos para el candidato', 0
    except Exception as e:
        print('No pasaron las pruebas de registro\n ', e)
        return 'No pasaron las pruebas registro con datos incorrectos para el candidato', 0


def register_invalid_candidate():
    try:
        print('Inicia el registro invalido')
        results = []
        for data in data_payloads:
            _, result = register400_candidate(data.copy(), 400 if data["email"] else 409)
            results.append(result)
            print('\n')
        print('Los resultados son:', results)
        casos = len(results)
        exito = sum(results)
        fallo = casos - exito
        print('pasaron:', exito)
        print('fallaron:', fallo)
        if exito == casos:
            headers, email_candidate, _ = step_register_candidate()
            print('Se hicieron las pruebas de registro para un usuario candidato con datos incorrectos')
            return 'Se hicieron las pruebas de registro para un usuario candidato con datos incorrectos', headers, email_candidate, 1
        else:
            headers, email_candidate, _ = step_register_candidate()
            print('No pasaron las pruebas de registro')
            return 'No pasaron las pruebas de registro con datos incorrectos', headers, email_candidate, 0
    except Exception as e:
        print('No pasaron las pruebas de registro', e)
        return 'No pasaron las pruebas de registro con datos incorrectos', None, None, 0




