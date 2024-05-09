from objetos.funciones import sendPostHeaders, base, sendPut


def paso4(vacantId, headers):
    try:
        url = base + 'vacancy/management/step4/' + vacantId
        myBody = {
            "newQuestions": [
                {
                    "question": "hola mundo",
                    "type": "SOFT_SKILL",
                    "typeQuestion": "CERRADA",
                    "isArmed": False,
                    "exclud": False,
                    "typeAnswer": True
                }
            ]
        }
        sendPostHeaders(url, headers, myBody, 200)
        print('se hizo el paso 4 de la creacion de la vacante')
        return 'se hizo el paso 4 de la creación de la vacante'
    except Exception as e:
        print('No se hizo el paso 4 de la creación de vacante', e)
        return 'No se hizo el paso 4 de la creación de la vacante'


def paso5(vacantId, headers):
    try:
        url = base + 'vacancy/management/step5/' + vacantId
        myBody = {
            "listVacantPsychometricTestInvolve": [],
            "newQuestions": [
                {
                    "exclud": False,
                    "type": "VIDEO",
                    "question": "hola mundo",
                    "typeQuestion": "CERRADA",
                    "isArmed": False
                },
                {
                    "exclud": False,
                    "type": "VIDEO_S",
                    "question": "¿Qué experiencias tienes en el uso de software contable y ERP?  ",
                    "typeQuestion": "CERRADA",
                    "isArmed": False
                }
            ]
        }
        sendPostHeaders(url, headers, myBody, 200)
        print('Se hizo el paso 5 de la creación de la vacante')
        return 'Se hizo el paso 5 de la creación de la vacante'
    except Exception as e:
        print('No se hizo el paso 5 de la creación de la vacante', e)
        return 'No se hizo el paso 5 de la creación de la vacante'


def paso6(vacantId, headers, recruiterId):
    try:
        url = base + 'vacancy/management/step6/' + vacantId
        myBody = {
            "recruiters": [
                {
                    "Notifications": True,
                    "type": "AUXILIAR",
                    "recruiterId": recruiterId
                }
            ]
        }
        sendPostHeaders(url, headers, myBody, 200)
        print('\n Se hizo el paso 6 de la creación de la vacante')
        return 'Se hizo el paso 6 de la creación de la vacante'
    except Exception as e:
        print('\n No se hizo el paso 6 de la creación de la vacante', e)
        return 'No se hizo el paso 6 de la creación de la vacante'


def paso7(vacantId, headers):
    try:
        url = base + 'vacancy/management/actived?vacantId=' + vacantId + '&approved=false'
        sendPut(url, headers, 200)
        print('\n Se publico la vacante correctamente')
        return 'Se publico la vacante correctamente'
    except Exception as e:
        print('\n No se publico la vacante', {e})
        return 'No se publico la vacante'
