from objetos.funciones import nombres, apellidos, base, sendPatch, foto, subirArchivo, \
    sendPostHeadersSinBody, sendPut
from test.login import login

respuesta, headers, recruiterID = login()


def nombrePerfil(headers):
    try:
        nombre = nombres()
        apellidoP = apellidos()
        apellidoM = apellidos()

        myBody = [
            {
                "op": "replace",
                "path": "/user/name",
                "value": nombre
            },
            {
                "op": "replace",
                "path": "/user/lastName",
                "value": apellidoP
            },
            {
                "op": "replace",
                "path": "/user/secondLastName",
                "value": apellidoM
            }
        ]

        url = base + 'user/recruiter'
        sendPatch(url, headers, myBody, 200)
        print('se cambian los nombres')
        return 'Se subieron los nombres correctamente'
    except Exception as e:
        print('\n no se hizo el cambio de los nombres', e)
        return 'No se subio el cambio de los nombres'


def fotoPerfil(headers):
    try:
        urlfoto = base + 'files/upload/uploadFile?typeFile=URL_PHOTO'
        ruta = foto()
        print(ruta)
        subirArchivo(ruta, urlfoto, headers, 201)
        print('\n Se subio la foto de perfil')
        return 'Se subio la foto de perfil'
    except Exception as e:
        print('\n No se subio la foto de perfil', e)
        return 'No se subio la foto de perfil'

def cambioPass(headers):
    try:
        urlPass = base + 'auth/verify-password?password=Abcd.1234'
        sendPostHeadersSinBody(urlPass, headers, 200)
        print('\n se hizo la solicitud de cambio de contraseña')
        urlPass2 = base + 'auth/change-password?newPassword=Abcd.1234'
        sendPut(urlPass2, headers, 200)
        print('\n se cambio la contraseña')
        return 'Se cambio la contraseña'
    except Exception as e:
        print('\n No se subio el cambio de la contraseña', e)
        return 'No se subio el cambio de la contraseña'

def cambioEmail(headers):
    try:
        urlEmail = base + 'auth/change-email?newEmail=huguito.reclutad2@yopmail.com&password=Abcd.1234'
        sendPostHeadersSinBody(urlEmail, headers, 200)
        print('\n Se mando el cambio de email correctamente')
        return 'Se mando el cambio de email correctamente'
    except Exception as e:
        print('\n No se pudo hacer el cambio de email', e)
        return 'no se mando el cambio de email'


