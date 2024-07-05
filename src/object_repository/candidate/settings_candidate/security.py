import random
from src.object_repository.candidate.registroCand.registerValid.stepRegisterCandidate import step_permission_candidate
from src.services.catalogs import data_user, env
from src.services.peticiones_HTTP import send_post_headers_sin_body, send_put, send_post_headers, send_delete_sin_body
from src.modules.Candidate.loginCand import login_cand, pass_email, email_candidate
from src.modules.Candidate.registerOnboading import register_onboarding_candidate
from src.object_repository.candidate.registroCand.dataNoValidCandidate.register_data_no_valid.legalesInvalido import \
    generate_combinations


def change_email_candidate(headers):
    try:
        print('Se inicia el cambio de email del candidato\n')
        _, _, _, _, new_email = data_user(env)
        url = env["URL_SERVER"] + 'auth/change-email?newEmail=' + new_email + '&password=' + pass_email
        respuesta = send_post_headers_sin_body(url, headers, 200)
        if respuesta != 0:
            print(f'Se manda el cambio de email {respuesta}\n')
            url = env["URL_SERVER"] + 'auth/verify-change-email?newEmail=' + new_email
            verificacion = send_post_headers_sin_body(url, headers, 200)
            print(f'Se activa el nuevo email {verificacion}\n')
            _, headers, _, _, _ = login_cand(new_email, pass_email)

            url = env["URL_SERVER"] + 'auth/change-email?newEmail=huguito.candidato.es@yopmail.com&password=' + pass_email
            send_post_headers_sin_body(url, headers, 200)
            url = env["URL_SERVER"] + 'auth/verify-change-email?newEmail=huguito.candidato.es@yopmail.com'
            send_post_headers_sin_body(url, headers, 200)
            print('Se regresa al email original\n')
            return 'Se manda el cambio y activacion del nuevo email', 1
        else:
            print('No se pudo hacer el cambio de email\n')
            return 'No se realizo el cambio de nuevo email', 0
    except Exception as e:
        print('No se pudo hacer el cambio de email', e)
        return 'No se realizo el cambio de nuevo email'


def change_phone(headers):
    try:
        print('Se inicia el cambio de teléfono\n')
        ladas = ['52', '34', '57']
        lada = random.choice(ladas)
        if lada != '34':
            phone = env["PHONE_OTHER"]
        else:
            phone = env["PHONE_ESP"]

        url = env["URL_SERVER"] + 'auth/change-phone?phone=' + phone + '&password=Abcd.1234&phoneCode=%2B' + lada
        resultado = send_post_headers_sin_body(url, headers, 200)
        if resultado != 0:
            print(f'Se manda un nuevo numero de teléfono: {phone}\n')
            return 'Se hizo el cambio de numero de teléfono', lada, phone, 1
        else:
            print('No se hizo el cambio de telefono \n')
            return 'No se realizo el cambio de numero de teléfono', None, None, 0
    except Exception as e:
        print('No se hizo el cambio de telefono \n', e)
        return 'No se realizo el cambio de numero de teléfono', None, None, 0


def verify_change_phone(headers, lada, phone):
    try:
        print('Se inicia la verificación del teléfono \n')
        url = env["URL_SERVER"] + 'auth/verify-code-sms?code=110901&phone=' + phone + '&phoneCode=%2B' + lada
        resultado = send_post_headers_sin_body(url, headers, 200)
        if resultado != 0:
            print('Se verifico el número correctamente \n')
            return 'Se verifico el número correctamente', 1
        else:
            print('No se verifico el número \n')
            return 'No se verifico el numero', 0
    except Exception as e:
        print(f'No se verifico el número {e}\n')
        return 'No se verifico el numero', 0


def change_pass_candiate(headers):
    try:
        print('Inicia el cambio de contraseña\n')
        url = env["URL_SERVER"] + 'auth/verify-password?password=Abcd.1234'
        resultado = send_post_headers_sin_body(url, headers, 200)
        if resultado != 0:
            print('Se manda a verificar la contraseña actual')
            url = env["URL_SERVER"] + 'auth/change-password?newPassword=Abcd.1234'
            send_put(url, headers, 200)
            print('Se cambia la contraseña del candidato \n')
            return 'Se cambia la contraseña del candidato', 1
        else:
            print('No se hizo el cambio de contraseña\n')
            return 'No se realizo el cambio de la contraseña', 0
    except Exception as e:
        print(f'No se hizo el cambio de contraseña {e}\n')
        return 'No se realizo el cambio de la contraseña', 0


def change_permisssion(headers):
    try:
        print('Inicia el cambio de permisos\n')
        url = env["URL_SERVER"] + 'user/permissions/register-list'
        print('Se mandan las combinaciones del los permisos \n')
        bodies = generate_combinations()
        n = 1
        for body in bodies:
            print("combinacion", n)
            send_post_headers(url, headers, body, 200)
            n += 1
        step_permission_candidate(headers)
        print('Se cambian los permisos del candidato\n')
        return 'Se cambiaron los permisos del candidato', 1
    except Exception as e:
        print(f'No se cambiaron los permisos {e}\n')
        return 'No se cambiaron los permisos', 0


def delete_account():
    try:
        print('Inicia la eliminacion de cuentan')
        _, email_candidate, _, _ = register_onboarding_candidate()
        _, headers, _, _, _ = login_cand(email_candidate, pass_email)
        url = env["URL_SERVER"] + 'management/user/delete-account?password=Abcd.1234'
        resultado = send_delete_sin_body(url, headers, 200)
        if resultado != 0:
            print('Se elmina la cuenta correctamente\n')
            return 'Se elmina la cuenta correctamente', 1
        else:
            print('No se elimino la cuenta\n')
            return 'No se elimino la cuenta', 0
    except Exception as e:
        print('No se elimino la cuenta\n', e)
        return 'No se elimino la cuenta', 0








