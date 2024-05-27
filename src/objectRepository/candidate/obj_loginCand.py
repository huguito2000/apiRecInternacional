from src.services.funciones import base, send_post

correo = "huguito.candidato.es@yopmail.com"


def step_login_candidate(correo):
    try:
        my_body = {
            "email": correo,
            "password": "Abcd.1234",
        }
        url = base + 'auth/login'
        resultado, headers = send_post(url, my_body, 200)
        token = headers['token']

        candidate_id = resultado['candidateId']

        print('el token es:' + token)
        headers = {
            'Authorization': f'Bearer {token}'
        }
        print('se realizo el login')
        return resultado, candidate_id, headers
    except Exception as e:
        print('No se hizo el login', e)
        return 'No se hizo el login'









