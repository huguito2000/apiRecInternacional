from dotenv import dotenv_values

from src.services.peticiones_HTTP import send_post_headers, base, send_put

env = dotenv_values("etc/.env")

def question_soft_skill(vacant_id, headers):
    try:
        url = env["URL_SERVER"] + 'vacancy/management/step4/' + vacant_id
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
        print('se hizo las preguntas de habilidades blandas')
        return 'se hizo las preguntas de habilidades blandas'
    except Exception as e:
        print('No se hizo las preguntas de habilidades blandas', e)
        return 'No se hizo las preguntas de habilidades blandas'


def video_psicometricas(vacant_id, headers):
    try:
        url = env["URL_SERVER"] + 'vacancy/management/step5/' + vacant_id
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
        print('Se hicieron las preguntas de psicometricas y video entrevoista')
        return 'Se hizo el paso 5 de la creación de la vacante'
    except Exception as e:
        print('No se hicieron las preguntas de psicometricas y video entrevoista', e)
        return 'No se hicieron las preguntas de psicometricas y video entrevoista'


def review_vacant(vacant_id, headers, recruiter_id):
    try:
        url = env["URL_SERVER"] + 'vacancy/management/step6/' + vacant_id
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


def post_vacancy(vacant_id, headers):
    try:
        url = env["URL_SERVER"] + 'vacancy/management/actived?vacantId=' + vacant_id + '&approved=false'
        code = send_put(url, headers, 200)
        assert code == 200
        print('\n Se publico la vacante correctamente')
        return 'Se publico la vacante correctamente'
    except Exception as e:
        print('\n No se publico la vacante', {e})
        return 'No se publico la vacante'
