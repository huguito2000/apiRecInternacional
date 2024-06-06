from dotenv import dotenv_values

from src.services.peticiones_HTTP import base, send_post

env = dotenv_values("etc/.env")


def step_login_recruiter(email, pass_email):
    try:
        my_body = {
            "email": email,
            "password": pass_email
        }
        url = env["URL_SERVER"] + 'auth/login'
        resultado, headers = send_post(url, my_body, 200)
        token = headers['token']
        print('se realizo el login')
        headers = {
            'Authorization': f'Bearer {token}'
        }
        return resultado, headers
    except Exception as e:
        print('\n No se hizo el login', e)
        return 'no se hizo el login'




