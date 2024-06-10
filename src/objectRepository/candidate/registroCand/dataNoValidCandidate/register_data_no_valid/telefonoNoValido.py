from dotenv import dotenv_values
from src.services.peticiones_HTTP import base, send_post_headers_sin_body
from src.objectRepository.candidate.registroCand.registerValid.stepRegisterCandidate import step_phone_candidate, \
    step_verify_code_cand


env = dotenv_values("etc/.env")
data_payloads = [
    "",
    " ",
    "41111111114",
    "11",
    "hola",
    "12345678901",
    "!@#$%^&*()",
    "123 456 7890",
    "999999990"
]


def step_phone_invalid_candidate(headers):
    print('Se inicia el envio de telefonos invalidos')
    global code
    try:
        print('Enviado numeros de telefono ...')
        url = env["URL_SERVER"] + 'auth/send-sms?phone='
        for nums_variation in data_payloads:
            full_url = url + str(nums_variation) + '&phoneCode=%2B34'
            code = send_post_headers_sin_body(full_url, headers, 412)
            print(f"  - Se envió el telefono: {nums_variation}")
        print('el codigo del numero es: ' + str(code))
        code = step_phone_candidate(headers)
        print('Se manda la sección de numeros de telefono icorrectos :) \n')
        return 'Se manda la sección de numeros de telefono icorrectos', code
    except Exception as e:
        print('No se obtuvo el codigo :( \n', e)


data_codes = [
    "",
    " ",
    "12345678",
    "1111",
    "holaMundo",
    "110901"
]


def step_verify_code_invalido_cand(headers):
    print('Inicia la verificacion del codigo')
    global respuesta
    try:
        print('Enviado los codigos ...')
        url = env["URL_SERVER"] + 'auth/verify-code-sms?code='

        for codes_variation in data_codes:
            full_url = url + str(codes_variation) +'&phone=999999990&phoneCode=%2B52'
            respuesta = send_post_headers_sin_body(full_url, headers, 412)
            print(f"  - Se envió el codigo: {codes_variation}")
        step_verify_code_cand(headers)
        print('Se valida la seccion de verificar el codigo con datos incorrectos :)\n', respuesta)
        return 'Se valida la seccion de verificar el codigo con datos incorrectos'
    except Exception as e:
        print(f'No se verifico el codigo {e}')
        return f'No se pudos hacer la verificación del codigo {e}'

