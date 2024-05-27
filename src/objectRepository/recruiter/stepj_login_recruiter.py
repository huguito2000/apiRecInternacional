from src.services.funciones import base, send_post

correo = "1104@yopmail.com"

def step_login_recruiter(correo):
    try:
        my_body = {
            "email": correo,
            "password": "Abcd.1234"
        }
        url = base + 'auth/login'
        resultado, headers = send_post(url, my_body, 200)
        token = headers['token']
        print('se realizo el login')
        print('el token es este:', token)
        headers = {
            'Authorization': f'Bearer {token}'
        }
        return resultado, headers
    except Exception as e:
        print('\n No se hizo el login', {e})
        return 'no se hizo el login'



