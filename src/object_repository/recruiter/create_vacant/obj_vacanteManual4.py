from src.services.catalogs import env
from src.services.peticiones_HTTP import send_post_headers, base, send_put


def question_soft_skill(vacant_id, headers):
    try:
        print('Inicia la creacion de cuestionario de habilidades blandas')
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
        respuesta = send_post_headers(url, headers, my_body, 200)
        if respuesta != 0:
            print('se hizo las preguntas de habilidades blandas :) \n')
            return 'se hizo las preguntas de habilidades blandas', 1
        else:
            print('No se hicieron las preguntas de habilidades blandas \n')
            return 'No se hicieron las preguntas de habilidades blandas', 0
    except Exception as e:
        print('No se hizo las preguntas de habilidades blandas :( \n', e)
        return 'No se hizo las preguntas de habilidades blandas', 0


def video_psicometricas(vacant_id, headers):
    try:
        print('Inicia la creacion de preguntas de video entrevista')
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
        resultado = send_post_headers(url, headers, my_body, 200)
        if resultado != 0:
            print('Se hicieron las preguntas de psicometricas y video entrevista :) \n')
            return 'Se hizo el paso 5 de la creación de la vacante', 1
        else:
            print('No se las rpeguntas de video entrevista\n')
            return 'No se hicieron las preguntas de video entrevista', 0
    except Exception as e:
        print('No se hicieron las preguntas de psicometricas y video entrevista :( \n', e)
        return 'No se hicieron las preguntas de psicometricas y video entrevista', 0


def review_vacant(vacant_id, headers, recruiter_id):
    try:
        print('Inicia la revisión de la vacante')
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
        resultado = send_post_headers(url, headers, my_body, 200)
        if resultado != 0:
            print('Se hizo el paso de revision de la creación de la vacante :) \n')
            return 'Se hizo el paso de la revisión de la creación de la vacante', 1
        else:
            print('No se hizo la revición de la vacante\n')
            return 'No se hizo la recvicion de la vacante', 0
    except Exception as e:
        print('No se hizo el paso de revisión de la creación de la vacante :( \n', e)
        return 'No se hizo el paso 6 de la creación de la vacante', 0


def post_vacancy(vacant_id, headers):
    try:
        print('Inicia la publicación de la vacante ')
        url = env["URL_SERVER"] + 'vacancy/management/actived?vacantId=' + vacant_id + '&approved=false'
        code = send_put(url, headers, 200)
        if code != 0:
            print('Se publico la vacante correctamente :) \n')
            return 'Se publico la vacante correctamente', 1
        else:
            print('No se publico la vacante')
            return 'No se publico la vacante', 0
    except Exception as e:
        print('No se publico la vacante :( \n', e)
        return 'No se publico la vacante', 0
