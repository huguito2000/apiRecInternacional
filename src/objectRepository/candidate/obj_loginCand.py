from dotenv import dotenv_values
from src.services.peticiones_HTTP import base, send_post

env = dotenv_values("etc/.env")
correo = "huguito.candidato.es@yopmail.com"


def step_login_candidate(correo):
    try:
        my_body = {
            "email": correo,
            "password": "Abcd.1234",
        }
        url = env["URL_SERVER"] + 'auth/login'
        resultado, headers = send_post(url, my_body, 200)

        token = headers['token']

        candidate_id = resultado['candidateId']

        headers = {
            'Authorization': f'Bearer {token}'
        }
        print('se realizo el login correctamente')
        return resultado, candidate_id, headers
    except Exception as e:
        print('No se hizo el login', e)
        return 'No se hizo el login'









