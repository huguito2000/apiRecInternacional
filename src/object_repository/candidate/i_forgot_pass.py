from src.services.catalogs import env
from src.services.peticiones_HTTP import send_post_sin_body, send_post_headers_sin_body

email_candidate = env["EMAIL_CANDIDATE_HAPPY_PATH"]


def i_forgot_password():
    try:
        url = env["URL_SERVER"] + 'auth/petition-restore-pass?email=' + email_candidate
        resultado = send_post_sin_body(url, 200)
        if resultado != 0:
            print('Se mandan la petición de solicitud de olvide mi contraseña\n')
            return 'Se manda la petición de la solicitud de camnio de contraseña correctamente', 1
        else:
            print('No se mando la solicitud de olvide mi contraseña\n')
            return 'No se mando la solicitud de olvide mi contraseña', 0
    except Exception as e:
        print('No se mando la solicitud de olvide mi contraseña\n', e)
        return 'No se mando la solicitud de olvide mi contraseña', 0


def confirm_restore_pass(headers):
    try:
        url = env["URL_SERVER"] + 'auth/confirm-restore-pass?password=Abcd.1234'
        resultado = send_post_headers_sin_body(url, headers, 200)
        if resultado != 0:
            print('Se manda la nueva contraseña\n')
            return 'Se manda confirmación de nueva contraseña de manera correcta', 1
        else:
            print('No se mando la nueva contraseña\n')
            return 'No se mando la nueva contraseña', 0
    except Exception as e:
        print('No se mando la nueva contraseña\n', e)
        return 'No se mando la nueva contraseña', 0

