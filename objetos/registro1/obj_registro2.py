from objetos.funciones import sendPostHeadersSinBody
from objetos.funciones import base

myBody ={}
def registro2(headers, correo, code):
    try:
        url = base + 'auth/verify-email?email=' + correo + '&code=' + code
        print(url)
        sendPostHeadersSinBody(url, headers, 200)
        print('Se realizo el segundo paso del registro')
        return 'Se realizo el segundo paso del registro'
    except Exception as e:
        print('No se realizo el paso 2 del registro', e)
        return 'No se realizo el paso 2 del registro'