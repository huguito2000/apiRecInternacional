from dotenv import dotenv_values

from src.services.catalogs import env
from src.services.peticiones_HTTP import base, send_post


def step_login_recruiter(email, pass_email):
    try:
        my_body = {
            "email": email,
            "password": pass_email
        }
        url = env["URL_SERVER"] + 'auth/login'
        resultado, headers = send_post(url, my_body, 200)
        if resultado != 0:
            token = headers['token']
            print('se realizo el login')
            headers = {
                'Authorization': f'Bearer {token}'
            }
            recruiter = resultado['recruiterId']
            print('se obtuvo el recruiterID del login :) \n')
            return headers, recruiter, 1
        else:
            print("No se hizo el login\n")
            return 'No se hizo el login', None, 0
    except Exception as e:
        print('\n No se hizo el login', e)
        return 'no se hizo el login', None, 0





