from datetime import datetime
from src.services.funciones import base, send_post_headers_sin_body, send_post, send_post_headers

def email_new():
    now = datetime.now()
    correo = 'reclu' + str(now.day) + str(now.month) + str(now.minute) + str(now.second) + '@yopmail.com'
    print(correo)
    return correo
url = base + 'auth/registry/recruiter'

def step_registro_recruiter():
    try:
        correo = email_new()
        my_body = {
            "email": correo,
            "userRol": "RECRUITER_ADMIN",
            "keySystem": "MX",
            "password": "Abcd.1234",
            "phoneLine": "+52",
            "phone": "5569777077"
        }
        resultado, headers = send_post(url, my_body, 201)
        print('se mandan los datos')
        return resultado, headers, correo
    except Exception as e:
        print('No se realizo la primera parte del registro crearReportesRecruiter', {e})
        return 'No se realizo el primer paso del registro crearReportesRecruiter'

def step_verify_email(headers, correo, code):
    try:
        url = base + 'auth/verify-email?email=' + correo + '&code=' + code
        print(url)
        send_post_headers_sin_body(url, headers, 200)
        print('Se realizo el segundo paso del registro crearReportesRecruiter')
        return 'Se realizo el segundo paso del registro crearReportesRecruiter'
    except Exception as e:
        print('No se realizo el paso 2 del registro crearReportesRecruiter', {e})
        return 'No se realizo el paso 2 del registro crearReportesRecruiter'


def step_permissions(headers):
    try:
        url = base + 'user/permissions/register-list'
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
                "permissionType": "RECOMMENDATIONS"
            },
            {
                "status": True,
                "permissionType": "NEWSLETTER_INTERNAL"
            },
            {
                "status": True,
                "permissionType": "NEWSLETTER_EXTERNAL"
            }
        ]
        send_post_headers(url, headers, my_body, 200)
        print("se mandan el tercer paso del registro crearReportesRecruiter")
        return 'se mandan el tercer paso del registro crearReportesRecruiter'
    except Exception as e:
        print('No se mandaron las notificaiones', {e})
        return 'No se mandaron las notificaiones'

def step_register_complete(headers):
    try:
        url = base + 'auth/registry/recruiter/complete'
        my_body = {
            "name": "hugo",
            "lastName": "rodriguez",
            "companyName": "involve",
            "industryId": "40288088798a3b0501798a58c2cf0053",
            "invoiceNotification": True,
            "countryId": "2c9f936481969f0aaaa996a00e090001"
        }
        send_post_headers(url, headers, my_body, 200)
        print('Se manda el paso cuarto del registro reclutrador')
        return 'Se mando el paso cuatro del registro Recruiter'
    except Exception as e:
        print('No se mando el paso 4', {e})
        return 'No se mando el paso 4 '
