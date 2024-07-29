from dotenv import dotenv_values

from src.modules.Candidate.loginCand import pass_email
from src.modules.recruiter.login_recruiter import login_recruiter
from src.services.catalogs import foto, subir_archivo, nombres, apellidos, env
from src.services.peticiones_HTTP import base, send_post_headers_sin_body, send_put, send_patch, send_delete, \
    send_delete_sin_body


def photo_profile(headers):
    try:
        urlfoto = env["URL_SERVER"] + 'files/upload/uploadFile?typeFile=URL_PHOTO'
        ruta = foto()
        print(ruta)
        resultado = subir_archivo(ruta, urlfoto, headers, 201)
        if resultado != 0:
            print('Se subio la foto de perfil\n')
            return 'Se subio la foto de perfil', 1
        else:
            print('No se subio la foto de perfil\n')
            return 'No se subio la foto de perfil', 0
    except Exception as e:
        print('No se subio la foto de perfil\n', e)
        return 'No se subio la foto de perfil', 0


def delete_photo_recruiter(headers):
    try:
        url = env["URL_SERVER"] +"files/upload/delete-file?typeFile=URL_PHOTO"
        resultado = send_delete_sin_body(url, headers, 200)
        if resultado != 0:
            print('Foto eliminada exitosamente\n')
            return 'Foto eliminada exitosamente', 1
        else:
            print('No se elimino la foto \n')
            return 'No se elimino la foto', 0
    except Exception as e:
        print('No se elimino la foto', e)
        return 'No se elimino la foto', 0


def change_pass(headers):
    try:
        url_pass = env["URL_SERVER"] + 'auth/verify-password?password=Abcd.1234'
        respuesta = send_post_headers_sin_body(url_pass, headers, 200)
        if respuesta != 0:
            print('se hizo la solicitud de cambio de contraseña \n')
            url_pass2 = env["URL_SERVER"] + 'auth/change-password?newPassword=Abcd.1234'
            respuesta = send_put(url_pass2, headers, 200)
            if respuesta != 0:
                print('se cambio la contraseña \n')
            return 'Se cambio la contraseña', 1
        else:
            print('No se cambio la contraseña\n')
            return 'No se camnbio la contraseña', 0

    except Exception as e:
        print('\n No se subio el cambio de la contraseña\n', e)
        return 'No se subio el cambio de la contraseña', 0


def change_email(headers, new_email):
    try:
        print('Se inicia el cambio de email del candidato\n')
        url = env["URL_SERVER"] + 'auth/change-email?newEmail=' + new_email + '&password=' + pass_email
        respuesta = send_post_headers_sin_body(url, headers, 200)
        if respuesta != 0:
            print(f'Se manda el cambio de email {respuesta}\n')
            url = env["URL_SERVER"] + 'auth/verify-change-email?newEmail=' + new_email
            verificacion = send_post_headers_sin_body(url, headers, 200)
            if verificacion != 0:
                print(f'Se activa el nuevo email {verificacion}\n')
                _, headers, _, _, _ = login_recruiter(new_email, pass_email)

                url = env[
                          "URL_SERVER"] + 'auth/change-email?newEmail=huguito.reclutador.es@yopmail.com&password=' + pass_email
                resultado = send_post_headers_sin_body(url, headers, 200)
                if resultado != 0:
                    url = env["URL_SERVER"] + 'auth/verify-change-email?newEmail=huguito.reclutador.es@yopmail.com'
                    resultado = send_post_headers_sin_body(url, headers, 200)
                    if resultado != 0:
                        print('Se regresa al email original\n')
                        return 'Se manda el cambio y activacion del nuevo email', 1
        else:
            print('No se pudo hacer el cambio de email\n')
            return 'No se realizo el cambio de nuevo email', 0
    except Exception as e:
        print('No se pudo hacer el cambio de email\n', e)
        return 'No se realizo el cambio de nuevo email'


def name_profile(headers, nombre, apellido_p, apellido_m):
    try:
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
        print(my_body)
        respuesta = send_patch(url, headers, my_body, 200)
        if respuesta != 0:
            print('se cambian los nombres correctamente')
            return 'Se subieron los nombres correctamente', 1
        else:
            print('No cambio la sección de nombres')
            return 'No cambio la sección de nombres', 0
    except Exception as e:
        print('\n no se hizo el cambio de los nombres', e)
        return 'No se subio el cambio de los nombres'

