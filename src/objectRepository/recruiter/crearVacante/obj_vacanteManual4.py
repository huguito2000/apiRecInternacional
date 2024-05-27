from src.services.funciones import send_post_headers, base, send_put


def paso4(vacant_id, headers):
    try:
        url = base + 'vacancy/management/step4/' + vacant_id
        my_body = {
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
        send_post_headers(url, headers, my_body, 200)
        print('se hizo el paso 4 de la creacion de la vacante')
        return 'se hizo el paso 4 de la creación de la vacante'
    except Exception as e:
        print('No se hizo el paso 4 de la creación de vacante', e)
        return 'No se hizo el paso 4 de la creación de la vacante'


def paso5(vacant_id, headers):
    try:
        url = base + 'vacancy/management/step5/' + vacant_id
        my_body = {
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
        send_post_headers(url, headers, my_body, 200)
        print('Se hizo el paso 5 de la creación de la vacante')
        return 'Se hizo el paso 5 de la creación de la vacante'
    except Exception as e:
        print('No se hizo el paso 5 de la creación de la vacante', e)
        return 'No se hizo el paso 5 de la creación de la vacante'


def paso6(vacant_id, headers, recruiter_id):
    try:
        url = base + 'vacancy/management/step6/' + vacant_id
        my_body = {
            "recruiters": [
                {
                    "Notifications": True,
                    "type": "AUXILIAR",
                    "recruiterId": recruiter_id
                }
            ]
        }
        send_post_headers(url, headers, my_body, 200)
        print('\n Se hizo el paso 6 de la creación de la vacante')
        return 'Se hizo el paso 6 de la creación de la vacante'
    except Exception as e:
        print('\n No se hizo el paso 6 de la creación de la vacante', e)
        return 'No se hizo el paso 6 de la creación de la vacante'


def paso7(vacant_id, headers):
    try:
        url = base + 'vacancy/management/actived?vacantId=' + vacant_id + '&approved=false'
        code = send_put(url, headers, 200)
        assert code == 200
        print('\n Se publico la vacante correctamente')
        return 'Se publico la vacante correctamente'
    except Exception as e:
        print('\n No se publico la vacante', {e})
        return 'No se publico la vacante'
