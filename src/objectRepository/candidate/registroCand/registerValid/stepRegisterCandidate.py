import random
import json
from src.services.catalogs import data_user, env
from src.services.peticiones_HTTP import base, send_post, send_put, send_post_headers, send_post_headers_sin_body, \
    send_get_headers, send_get


def get_area(headers):
    url = env["URL_SERVER"] + "management/catalog/area"
    response: list = send_get_headers(url, headers, 200)
    try:
        num = random.randint(0, 10)
        area = response[num]['areaId']
        print('se optiene el area id:\n', area)
        return area
    except (json.JSONDecodeError, KeyError) as e:
        print(f'Error al obtener areaIds :( \n: {e}')


def get_nacionality():
    try:
        url = env["URL_SERVER"] + "management/catalog/nationality"
        response: list = send_get(url, 200)
        num = random.randint(0, 100)
        nationality_id = response[num]['nationalityId']
        return nationality_id
    except Exception as e:
        print('No se obtuvo la nacionalidad', e)
        return 'No se obtuvo la nacionalidad'


def step_register_candidate():
    try:
        print('\nInicia el proceso de registro del candidato')
        _, _, _, _, email_candidate = data_user(env)
        nationality_id = get_nacionality()
        my_body = {
            "email": email_candidate,
            "keySystem": "ESP",
            "acceptPrivacy": True,
            "acceptTerms": True,
            "nationalityId": nationality_id
        }

        url = env["URL_SERVER"] + 'auth/registry/candidate'
        resultado, headers = send_post(url, my_body, 201)
        if resultado != 0:
            headers = headers['token']
            token = headers.replace('Bearer ', '')
            headers = {
                'Authorization': f'Bearer {token}'
            }
            print('primer paso del registro exitoso')
            return headers, email_candidate, 1
        else:
            print('No paso el registro :(\n')
            return 'No paso el registro del candidato', None, 0
    except Exception as e:
        print('No paso el registro :(', e)
        return 'No paso el registro del candidato', None, 0


def step_create_pass_candidate(headers):
    try:
        print("\nse manda la contraseña...")
        password = 'Abcd.1234'
        url = env["URL_SERVER"] + 'auth/create-pass?password=' + password
        resultado = send_put(url, headers, 200)
        if resultado != 0:
            print('paso la creacion de la contraseña :)\n')
            return 'paso la creacion de la contraseña', 1
        else:
            print('No paso la creacion de la contraseña :(\n')
            return 'No paso la creación de la contraseña para el candidato', 0
    except Exception as e:
        print('No paso la creacion de la contraseña :(', e)
        return 'No paso la creación de la contraseña para el candidato', 0


def step_permission_candidate(headers):
    try:
        print('\nInicia el envio de permisos de notificaciones')
        my_body = [
            {
                "status": True,
                "permissionType": "NOTIFICATION_PROCESS"
            },
            {
                "status": True,
                "permissionType": "REMINDER"
            },
            {
                "status": True,
                "permissionType": "JOB_VACANCIES"
            },
            {
                "status": True,
                "permissionType": "NEWSLETTER_INTERNAL"
            },
            {
                "status": True,
                "permissionType": "NEWSLETTER_EXTERNAL"
            },
            {
                "status": True,
                "permissionType": "RECOMMENDATIONS"
            }
        ]
        url = env["URL_SERVER"] + 'user/permissions/register-list'
        resultado = send_post_headers(url, headers, my_body, 200)
        if resultado != 0:
            print('pasaron los permisos de notificaciones :)\n')
            return 'pasaron los permisos de notificaciones de candidato', 1
        else:
            print('No pasaron los permisos :(\n')
            return 'No pasaron los permisos del candidato', 0
    except Exception as e:
        print('No pasaron los permisos :(\n', e)
        return 'No pasaron los permisos del candidato', 0


def step_phone_candidate(headers):
    try:
        print('Inicia el registro del numero de teléfono valido')
        url = env["URL_SERVER"] + 'auth/send-sms?phone=999999990&phoneCode=%2B34'
        code = send_post_headers_sin_body(url, headers, 200)
        if code != 0:
            print('el codigo del numero es: ' + str(code), '\n')
            if code['message'] == "SMS enviado exitosamente.":
                code = '110901'
                print('Se actualizo el codigo actualizado a', code)
            print('Se mando el número de teléfono y se obtuvo el codigo :)\n')
            return code, 1
        else:
            print('No se obtuvo el codigo :(\n')
            return 'No se obtuvo el codigo del telefono del candidato', 0
    except Exception as e:
        print('No se obtuvo el codigo :(\n', e)
        return 'No se obtuvo el codigo del telefono del candidato', 0


def step_resend_code(headers):
    try:
        print('Se inicia el reenvio del codígo')
        url = env["URL_SERVER"] + 'auth/resend-sms?phone=999999990'
        code = send_post_headers_sin_body(url, headers, 200)
        if code != 0:
            print('volver a Enviar ' + str(code))
            return 'Se envio el codigo correctamente', 1
        else:
            print('No se reenvio el codigo :(\n')
            return 'No se puedo volver a enviar el codigo correctamente', 0
    except Exception as e:
        print('No se reenvio el codigo :(\n', e)
        return 'No se puedo volver a enviar el codigo correctamente', 0


def step_verify_code_cand(headers):
    try:
        print('Inicia la verificación del codigo obtenido')
        url = base + 'auth/verify-code-sms?code=110901&phone=999999990&phoneCode=%2B52'
        respuesta = send_post_headers_sin_body(url, headers, 200)
        if respuesta != 0:
            print('Se verifico el codigo correctamente :)\n')
            return 'Se verifico el codigo correctamente', 1
        else:
            print('No se verifico el codigo :(\n')
            return 'No se verifico el codigo :(\n', 0
    except Exception as e:
        print('No se verifico el codigo :(\n', e)
        return 'No se verifico el codigo :(\n', 0

"""
solo en caso de mexico
def obtener_code_candidate(headers):
    url = base + 'user/candidate'
    code = sendGet(url, headers, 200)
    print(url)
    print('este es el codigo' + str(code))
    code = code['user']
    code = code['checkCode']
    print(code)
    return code

"""


def step_names_candidate(headers, name, last_name, birth_date):
    try:
        print('Inicia el registro del formulario del nombre\n')
        area = get_area(headers)
        my_body = {
            "name": name,
            "lastName": last_name,
            "dateBirth": str(birth_date),
            "areaId": area,
            "cityId": "2c9f936481969f0cccc996a00e092521"
        }
        url = env["URL_SERVER"] + 'auth/registry/candidate/complete'
        resultado = send_post_headers(url, headers, my_body, 200)
        if resultado != 0:
            print('Se envia el formulario de nombres del candidato :)\n')
            return 'Se envia el formulario de nombres del candidato :)', 1
        else:
            print('No se envio el nombre del candidato :(\n')
            return 'No se envio el nombre del candidato :(\n', 0
    except Exception as e:
        print('No se envio el nombre del candidato :(\n', e)
        return 'No se envio el nombre del candidato :(\n', 0

