from datetime import datetime

from dotenv import dotenv_values

from src.services.catalogs import data_user
from src.services.peticiones_HTTP import base, send_post_headers_sin_body, send_post, send_post_headers
env = dotenv_values("etc/.env")


def step_register_recruiter():
    try:
        _, _, _, _, email = data_user(env)

        my_body = {
            "email": email,
            "userRol": "RECRUITER_ADMIN",
            "keySystem": "MX",
            "password": "Abcd.1234",
            "phoneLine": "+52",
            "phone": "5569777077"
        }

        url = env["URL_SERVER"] + 'auth/registry/recruiter'
        resultado, headers = send_post(url, my_body, 201)
        print('se mandan los datos')
        return resultado, headers, email
    except Exception as e:
        print('No se realizo la primera parte del registro create_report_recruiter', {e})
        return 'No se realizo el primer paso del registro create_report_recruiter'


def step_verify_email(headers, email, code):
    try:
        url = env["URL_SERVER"] + 'auth/verify-email?email=' + email + '&code=' + code
        print(url)
        send_post_headers_sin_body(url, headers, 200)
        print('Se realizo el segundo paso del registro create_report_recruiter')
        return 'Se realizo el segundo paso del registro create_report_recruiter'
    except Exception as e:
        print('No se realizo el paso 2 del registro create_report_recruiter', {e})
        return 'No se realizo el paso 2 del registro create_report_recruiter'


def step_permissions(headers):
    try:
        url = env["URL_SERVER"] + 'user/permissions/register-list'
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
        print("se mandan el tercer paso del registro create_report_recruiter")
        return 'se mandan el tercer paso del registro create_report_recruiter'
    except Exception as e:
        print('No se mandaron las notificaiones', {e})
        return 'No se mandaron las notificaiones'


def step_register_complete(headers):
    try:
        url = env["URL_SERVER"] + 'auth/registry/recruiter/complete'
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

