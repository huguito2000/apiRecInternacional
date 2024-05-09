from objetos.funciones import sendPut, sendPatch, sendPostSinBody, sendPost
from datetime import datetime
from objetos.funciones import base
now = datetime.now()
correo = 'reclu' + str(now.day) + str(now.month) + str(now.minute) + str(now.second) + '@yopmail.com'
print(correo)
url = base + 'auth/registry/recruiter'

def registro1():
    try:
        myBody = {
            "email": correo,
            "userRol": "RECRUITER_ADMIN",
            "keySystem": "MX",
            "password": "Abcd.1234",
            "phoneLine": "+52",
            "phone": "5569777077"
        }
        resultado, headers = sendPost(url, myBody, 201)
        print('se mandan los datos')
        return resultado, headers, correo
    except Exception as e:
        print('No se realizo la primera parte del registro')
        return 'No se realizo el primer paso del registro'



