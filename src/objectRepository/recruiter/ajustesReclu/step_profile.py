from dotenv import dotenv_values
from src.services.catalogs import foto, subir_archivo, nombres, apellidos
from src.services.peticiones_HTTP import base, send_post_headers_sin_body, send_put, send_patch

env = dotenv_values("etc/.env")

def photo_profile(headers):
    try:
        urlfoto = env["URL_SERVER"] + 'files/upload/uploadFile?typeFile=URL_PHOTO'
        ruta = foto()
        print(ruta)
        subir_archivo(ruta, urlfoto, headers, 201)
        print('\nSe subio la foto de perfil')
        return 'Se subio la foto de perfil'
    except Exception as e:
        print('\n No se subio la foto de perfil', e)
        return 'No se subio la foto de perfil'


def change_pass(headers):
    try:
        url_pass = env["URL_SERVER"] + 'auth/verify-password?password=Abcd.1234'
        send_post_headers_sin_body(url_pass, headers, 200)
        print('\n se hizo la solicitud de cambio de contraseña')
        url_pass2 = env["URL_SERVER"] + 'auth/change-password?newPassword=Abcd.1234'
        send_put(url_pass2, headers, 200)
        print('\n se cambio la contraseña')
        return 'Se cambio la contraseña'
    except Exception as e:
        print('\n No se subio el cambio de la contraseña', e)
        return 'No se subio el cambio de la contraseña'


def change_email(headers):
    try:
        url_email = env["URL_SERVER"] + 'auth/change-email?newEmail=huguito.reclutad2@yopmail.com&password=Abcd.1234'
        send_post_headers_sin_body(url_email, headers, 200)
        print('\n Se mando el cambio de email correctamente')
        return 'Se mando el cambio de email correctamente'
    except Exception as e:
        print('\n No se pudo hacer el cambio de email', e)
        return 'no se mando el cambio de email'


def name_profile(headers):
    try:
        nombre = nombres()
        apellido_p = apellidos()
        apellido_m = apellidos()

        my_body = [
            {
                "op": "replace",
                "path": "/user/name",
                "value": nombre
            },
            {
                "op": "replace",
                "path": "/user/lastName",
                "value": apellido_p
            },
            {
                "op": "replace",
                "path": "/user/secondLastName",
                "value": apellido_m
            }
        ]

        url = env["URL_SERVER"] + 'user/recruiter'
        send_patch(url, headers, my_body, 200)
        print('se cambian los nombres')
        return 'Se subieron los nombres correctamente'
    except Exception as e:
        print('\n no se hizo el cambio de los nombres', e)
        return 'No se subio el cambio de los nombres'

