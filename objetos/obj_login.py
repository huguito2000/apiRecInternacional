from objetos.funciones import base
from objetos.funciones import sendPost

myBody = {
    "email": "1104@yopmail.com",
    "password": "Abcd.1234"
}

def hacerLogin():
    try:
        url = base + 'auth/login'
        resultado, headers = sendPost(url, myBody, 200)
        token = headers['token']
        print('se realizo el login')
        print('el token es este:', token)
        headers = {
            'Authorization': f'Bearer {token}'
        }
        return resultado, headers, token
    except Exception as e:
        print('\n No se hizo el login', e)
        return 'no se hizo el login'



