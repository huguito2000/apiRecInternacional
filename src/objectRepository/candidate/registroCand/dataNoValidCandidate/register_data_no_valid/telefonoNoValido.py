from src.objectRepository.candidate.registroCand.registerValid.stepRegisterCandidate import step_phone_candidate, \
    step_verify_code_cand
from src.services.funciones import base, send_post_headers_sin_body

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

def step_tel_invalido_cand(headers):
    global code
    try:
        print('Enviado numeros de telefono ...')

        url = base + 'auth/send-sms?phone='

        for nums_variation in data_payloads:
            full_url = url + str(nums_variation) + '&phoneCode=%2B34'
            code = send_post_headers_sin_body(full_url, headers, 412)
            print(f"  - Se envió el telefono: {nums_variation}")
        print('el codigo del numero es: ' + str(code))
        code = step_phone_candidate(headers)
        return code
    except Exception as e:
        print('No se obtuvo el codigo', e)


data_codes = [
    "",
    " ",
    "12345678",
    "1111",
    "holaMundo",
    "110901"
]
def step_verify_code_invalido_cand(headers):
    global respuesta
    try:
        print('Enviado los codigos ...')
        url = base + 'auth/verify-code-sms?code='

        for codes_variation in data_codes:
            full_url = url + str(codes_variation) +'&phone=999999990&phoneCode=%2B52'
            respuesta = send_post_headers_sin_body(full_url, headers, 412)
            print(f"  - Se envió el codigo: {codes_variation}")
        step_verify_code_cand(headers)
        print(respuesta)
        return 'Se envia los codigos incorrectos del telefono'
    except Exception as e:
        print(f'No se verifico el codigo {e}')
        return f'No se verifico el codigo {e}'