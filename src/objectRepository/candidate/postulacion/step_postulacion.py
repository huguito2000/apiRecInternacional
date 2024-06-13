import random
from dotenv import dotenv_values
from src.modules.recruiter.login_recruiter import login_recruiter
from src.services.catalogs import salary_min
from src.services.peticiones_HTTP import send_get_headers, base, send_post_headers_sin_body, send_post_headers

env = dotenv_values("etc/.env")
email_candidate = env["EMAIL_CANDIDATE_HAPPY_PATH"]
email = env["EMAIL_RECRUITER_HAPPY_PATH"]


# se obtiene el ID de la vacanbe regresado el mismo
def get_vacante_id():
    try:
        print('\ninicia el login del reclutador', email)
        _, headers, _ = login_recruiter(email)
        url = env[
                  "URL_SERVER"] + 'user/vacant/admin?pageSize=6&pageNumber=0&sortBy=publicationDate&sortDirection=DESC&status=ACTIVA'
        response = send_get_headers(url, headers, 200)
        vacant_id = response["content"][0]["vacant"]["vacantId"]
        print('la vacanteId es: ' + vacant_id)
        return vacant_id
    except Exception as e:
        print('No se obtuvo la vacant Id', e)
        return 'No se obtuvo la vacant ID'


# se obtiene el id de las preguntas una vez que te postulas
def get_preguntas(headers, url, cantidad):
    try:
        questions: list = []
        resultado = send_get_headers(url, headers, 200)
        for i in range(cantidad):
            questions.append(str((resultado['content'][i]['questionId'])))
        print('Se obtienen los Ids de las preguntas')

        return questions
    except Exception as e:
        print('No se pudo obtener los ids de las preguntas', e)
        return 'No se pudo obtener los ids de las preguntas'


# Se hace la postulacion de la primera vacante que se encuentra

def postulacion(headers):
    try:
        print("\nInicia el proceso de postulacion")
        vacant_id = get_vacante_id()
        url = env["URL_SERVER"] + 'user/candidate/postulation?vacantId=' + vacant_id
        print(url)
        postulation_id = send_post_headers_sin_body(url, headers, 200)
        print('la postulacion es: ', postulation_id)
        print('se hizo la postulacion correctamente')
        return 'se realizo la postulación a una vacante', postulation_id
    except Exception as e:
        print('No se hizo la postulacion', e)
        return 'No se hizo la postulación a una vacante'


# se saca de manera aleatoria un nuemro entre el rango de 1 a 5
def experiencia():
    exp = random.randint(1, 5)
    return exp


# Se manda la experiencia laboral
def exp_laboral_cuestionario(headers, postulation_id):
    try:
        print('Se envia el cuentionario de experiencia laboral\n')
        exp1 = int(experiencia())
        exp2 = int(experiencia())
        url = env[
                  "URL_SERVER"] + 'user/candidate/postulation/question?page=0&size=100&processId=' + postulation_id + '&questionnaire=AREA_SPECIALTY'

        preguntas = get_preguntas(headers, url, 2)
        print(preguntas[0])
        print(preguntas[1])

        my_body = [
            {
                "question": {
                    "questionId": preguntas[0]
                },
                "value": exp1,
                "yearsExperienceAnswer": exp1
            },
            {
                "question": {
                    "questionId": preguntas[1]
                },
                "value": exp2,
                "yearsExperienceAnswer": exp2
            }
        ]

        url = env[
                  "URL_SERVER"] + 'user/candidate/postulation/answer?processId=' + postulation_id + '&questionnaire=EXPERIENCE'
        print(url)
        resultado = send_post_headers(url, headers, my_body, 200)
        print('Se mandaron las respuestas del cuentionario :)\n', resultado)
        return ('Se respondieron las preguntas del cuestionario en la sección'
                ' de experiencia laboral, exitosamente')
    except Exception as e:
        print('No se mando las respuestas del cuestionario :(\n', e)
        return 'no se mando las respuestas del cuestionario'


# se obtienen los niveles aleatoriamente
niveles = ['INTERMEDIO', 'AVANZADO', 'EXPERTO']
nivel = random.choice(niveles)


# se mandan las preguntas de habilidad profesional
def habilidad_profesional(headers, postulation_id):
    try:
        print('inicia las habilidades profesionales \n')
        url = env[
                  "URL_SERVER"] + 'user/candidate/postulation/question?page=0&size=100&processId=' + postulation_id + '&questionnaire=HARD_SKILL'

        preguntas = get_preguntas(headers, url, 1)
        print(preguntas)
        my_body = [
            {
                "question": {
                    "questionId": str(preguntas[0])
                },
                "value": nivel,
                "levelHardSkill": nivel
            }
        ]
        print(my_body)
        url = env[
                  "URL_SERVER"] + 'user/candidate/postulation/answer?processId=' + postulation_id + '&questionnaire=HARD_SKILL'
        respuesta = send_post_headers(url, headers, my_body, 200)
        print('se envio el cuestionario de habilidades profesionales :)\n', respuesta)
        return 'Se envian las respuestas de las habilidades profesionales'
    except Exception as e:
        print('No se envian respuestas de las habilidades profesionales :(\n', e)
        return 'No se envian las habilidades profesionales'


def habilidad_blandas(headers, postulation_id):
    try:
        print('inicia las habilidades blandas \n')
        url = env[
                  "URL_SERVER"] + 'user/candidate/postulation/question?page=0&size=100&processId=' + postulation_id + '&questionnaire=SOFT_SKILL'

        preguntas = get_preguntas(headers, url, 1)
        print(preguntas[0])
        url = env[
                  "URL_SERVER"] + 'user/candidate/postulation/answer?processId=' + postulation_id + '&questionnaire=SOFT_SKILL'
        my_body = [
            {
                "question": {
                    "questionId": preguntas[0]
                },
                "value": True,
                "binaryAnswer": True
            }
        ]

        respuesta = send_post_headers(url, headers, my_body, 200)
        print('se envia las respuestas del habilidades blandas :)\n ', respuesta)
        return 'Se envian las respuestas de las habilidades blandas'
    except Exception as e:
        print('No se envia las respuestas de las habilidades balndas :(\n', e)
        return 'No se envia las respuestas de las habilidades balndas'


# se manda la expectativa salarial
def expectativa_salarial(headers, postulation_id):
    try:
        print('Inicia la espectava salarial :)\n')
        salario_min = salary_min()
        url = env["URL_SERVER"] + 'user/candidate/postulation/salary-expectation'
        my_body = {
            "selectionProcessId": postulation_id,
            "salaryMin": salario_min,
            "salaryMax": None,
            "periodicityId": "4028818e8e337efb018e33801b680005",
            "currencyId": "2c9f9364867665940186849ddb990011"
        }

        respuesta = send_post_headers(url, headers, my_body, 200)
        print('Se manda la espectativa salarial :)\n', respuesta)
        return 'Se envia la espectativa salarial correctamente'
    except Exception as e:
        print('No se mando la espectativa salarial :(\n', e)
        return 'No se manda la espectativa salarial'


# se manda las condiciones de contratacion
def condiciones_de_contratacion(headers, postulation_id):
    try:
        print('Inicia el egistro de condiciones de contratación')
        url = env["URL_SERVER"] + 'user/candidate/postulation/contract-conditions'
        my_body = {
            "selectionProcessId": postulation_id,
            "completeContractConditions": True,
            "detailsContractConditions": "tengo todo"
        }

        respuesta = send_post_headers(url, headers, my_body, 200)
        print('Se mandan las condiciones de contratación :)\n', respuesta)
        return 'Se envian las condiciones de contratación, correctamente'
    except Exception as e:
        print('No se mandan las condiciones de contratacion :(\n', e)
        return 'No se mandan las condiciones de contratacion'


# se manda los permisos de video presentacion y video entrevista
def seleccion_de_permisos(headers, postulation_id):
    try:
        print('Se inicia la seccion de permisos de videos y psicometricas')

        url = env["URL_SERVER"] + 'user/permissions/selection-process?selectionProcessId=' + postulation_id
        my_body = [
            {
                "permissionType": "VIDEOPRESENTATION_SHARE",
                "status": False
            },
            {
                "permissionType": "VIDEOINTERVIEW",
                "status": False
            }
        ]

        respuesta = send_post_headers(url, headers, my_body, 200)
        print('Se mandan los permisos de postulacion :)\n', respuesta)
        return 'Se envian los permisos de postulación'
    except Exception as e:
        print('No se mandan los permisos de postulacion :(\n', e)
        return 'No se mandan los permisos de postulación'


def change_permission_postulation():
    print('hola')