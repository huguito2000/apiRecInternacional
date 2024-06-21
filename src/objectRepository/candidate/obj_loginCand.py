from dotenv import dotenv_values

from src.services.catalogs import env
from src.services.peticiones_HTTP import send_post

email_candidate = env["EMAIL_CANDIDATE_HAPPY_PATH"]
pass_email = env["PASS_EMAIL_RECRUITER_HAPPY_PATH"]


def step_login_candidate(email_candidate, pass_email):
    try:
        print('Se inicia sesion con el candidato', email_candidate)
        my_body = {
            "email": email_candidate,
            "password": pass_email,
        }
        url = env["URL_SERVER"] + 'auth/login'
        resultado, headers = send_post(url, my_body, 200)
        if resultado != 0:
            token = headers['token']
            candidate_id = resultado['candidateId']
            headers = {
                'Authorization': f'Bearer {token}'
            }
            print('se realizo el login correctamente :)\n')
            return candidate_id, headers, 1
        else:
            print('No se hizo el paso del login')
            return 'No se hizo el paso del login', None, 0
    except Exception as e:
        print('No se hizo el login :(\n', e)
        return 'No se hizo el login', None, 0



