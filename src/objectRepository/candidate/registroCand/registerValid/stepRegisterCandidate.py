from datetime import datetime
from src.services.funciones import base, send_post, send_put, send_post_headers, send_post_headers_sin_body, nombres, apellidos


def email_new():
    now = datetime.now()
    correo = 'cand' + str(now.day) + str(now.month) + str(now.minute) + str(now.second) + '@yopmail.com'
    return correo


def step_register_candidate():
    try:
        correo = email_new()
        print(correo)
        my_body = {
            "email": correo,
            "keySystem": "ESP",
            "acceptPrivacy": True,
            "acceptTerms": True,
            "nationalityId": "40288086796ba27001796bbd39f70038"
        }
        url = base + 'auth/registry/candidate'
        resultado, headers = send_post(url, my_body, 201)
        headers = headers['token']
        token = headers.replace('Bearer ', '')
        headers = {
            'Authorization': f'Bearer {token}'
        }
        print(resultado)
        print(headers)
        return headers, correo
    except Exception as e:
        print('No paso el registro', e)
        return 'No paso el registro del candidato'

def step_create_pass_candidate(headers):
    try:
        print("se manda la contraseña...")
        password = "Abcd.1234"
        url = base + 'auth/create-pass?password=' + password
        send_put(url, headers, 200)
        print('paso la creacion de la contraseña')
        return 'paso la creacion de la contraseña'
    except Exception as e:
        print('No paso la creacion de la contraseña', e)
        return 'No paso la creación de la contraseña para el candidato'


def step_permission_candidate(headers):
    try:
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
        url = base + 'user/permissions/register-list'
        send_post_headers(url, headers, my_body, 200)
        print('no pasaron los permisos de notificaiones')
        return 'No pasaron los permisos de notificaciones de candidato'
    except Exception as e:
        print('No pasaron los permisos', e)
        return 'No pasaron los permisos del candidato'


def step_phone_candidate(headers):
    try:
        url = base + 'auth/send-sms?phone=999999990&phoneCode=%2B34'
        code = send_post_headers_sin_body(url, headers, 200)
        print('el codigo del numero es: ' + str(code))
        if code['message'] == "SMS enviado exitosamente.":
            code = '110901'
            print('Codigo actualizado a', code)
        return code
    except Exception as e:
        print('No se obtuvo el codigo', e)
        return 'No se obtuvo el codigo del telefono del candidato'


def step_resend_code(headers):
    try:
        url = base + 'auth/resend-sms?phone=999999990'
        code = send_post_headers_sin_body(url, headers, 200)
        assert code == 200
        print('volver a Enviar ' + str(code))
        return 'Se envio el codigo correctamente'
    except Exception as e:
        print('No se envio el codigo', e)
        return 'No se puedo volver a enviar el codigo correctamente'

def step_verify_code_cand(headers):
    try:
        url = base + 'auth/verify-code-sms?code=110901&phone=999999990&phoneCode=%2B52'
        respuesta = send_post_headers_sin_body(url, headers, 200)
        print(respuesta)
    except Exception as e:
        print('No se verifico el codigo', e)

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


def step_names_candidate(headers):
    name = nombres()
    last_name = apellidos()
    try:
        my_body = {
            "name": name,
            "lastName": last_name,
            "dateBirth": "2000-12-12",
            "areaId": "40288087797b055a01797b14e5f40036",
            "cityId": "2c9f936481969f0cccc996a00e092521"
        }

        url = base + 'auth/registry/candidate/complete'
        send_post_headers(url, headers, my_body, 200)
        print(' se en envia el nombre del candidato')
    except Exception as e:
        print('No se envio el nombre del candidato', e)