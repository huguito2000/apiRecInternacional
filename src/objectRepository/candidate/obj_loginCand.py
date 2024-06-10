from dotenv import dotenv_values
from src.services.peticiones_HTTP import base, send_post

env = dotenv_values("etc/.env")
email_candidate = env["EMAIL_CANDIDATE_HAPPY_PATH"]


def step_login_candidate(email_candidate):
    try:
        print('Se inicia sesion con el candidato', email_candidate)
        my_body = {
            "email": email_candidate,
            "password": "Abcd.1234",
        }
        url = env["URL_SERVER"] + 'auth/login'
        resultado, headers = send_post(url, my_body, 200)

        token = headers['token']

        candidate_id = resultado['candidateId']

        headers = {
            'Authorization': f'Bearer {token}'
        }
        print('se realizo el login correctamente :)\n')
        return resultado, candidate_id, headers
    except Exception as e:
        print('No se hizo el login :(\n', e)
        return 'No se hizo el login'









