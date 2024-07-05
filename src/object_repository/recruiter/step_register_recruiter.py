from src.services.catalogs import data_user, env
from src.services.peticiones_HTTP import send_post_headers_sin_body, send_post, send_post_headers


def step_register_recruiter(email):
    try:
        print('Se inicia el registro del reclutador')
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
        if resultado != 0:
            print('se mandan los datos para el registro de reclutador\n')
            code = str(resultado['user']['checkCode'])
            token = headers['token']
            token = str(token.replace('Bearer ', ''))
            headers = {
                'Authorization': f'Bearer {token}'
            }
            return code, headers, email, 1
        else:
            print('No se mandaron los datos para el registro\n')
            return 'No se mandaron los datos de registro', None, None, 0
    except Exception as e:
        print('No se realizo la primera parte del registro create_report_recruiter', e)
        return 'No se realizo el primer paso del registro create_report_recruiter', 0


def step_verify_email(code, headers, email):
    try:
        print('inica el la verificación de la cuenta')
        url = env["URL_SERVER"] + 'auth/verify-email?email=' + email + '&code=' + code
        respuesta = send_post_headers_sin_body(url, headers, 200)
        if respuesta != 0:
            print('Se realizo la verificación de la cuenta\n')
            return 'Se realizo la verificacion de la cuenta', 1
        else:
            print('No se verifico la cuenta\n')
            return 'No se verifico la cuenta', 0
    except Exception as e:
        print('No se realizo la verificacion de la cuenta\n', e)
        return 'No se realizo la verificación de la cuenta', 0


def step_permissions(headers):
    try:
        print('Inicia el envio de permisos')
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
        respuesta = send_post_headers(url, headers, my_body, 200)
        if respuesta != 0:
            print("Se mandan los permisos de notificaiones\n")
            return 'Se mandan los permisos', 1
        else:
            print("No se mandan los permisos de notificaciones\n")
            return 'No se mandan los permisos de notificaciones', 0

    except Exception as e:
        print('No se mandaron las notificaiones \n', e)
        return 'No se mandaron las notificaiones', 0


def step_register_complete(headers):
    try:
        print('Inicia el registro de nombres')
        url = env["URL_SERVER"] + 'auth/registry/recruiter/complete'
        my_body = {
            "name": "hugo",
            "lastName": "rodriguez",
            "companyName": "involve",
            "industryId": "40288088798a3b0501798a58c2cf0053",
            "invoiceNotification": True,
            "countryId": "2c9f936481969f0aaaa996a00e090001"
        }
        resultado = send_post_headers(url, headers, my_body, 200)
        if resultado != 0:
            print('Se manda el nombre del registro reclutrador\n')
            return 'Se mando el nombre del registro Recruiter', 1
        else:
            print('No se mando el nombre')
            return 'No se mando el nombre', 0
    except Exception as e:
        print('No se el nombre', e)
        return 'No se el nombre', 0

