import random
import requests
from src.modules.Candidate.loginCand import login_cand, pass_email
from src.modules.recruiter.login_recruiter import login_recruiter
from src.services.catalogs import salary_min, subir_archivo, videos, env
from src.services.peticiones_HTTP import send_get_headers, send_post_headers_sin_body, send_post_headers, \
    send_delete_sin_body


email_candidate = env["EMAIL_CANDIDATE_HAPPY_PATH"]
email = env["EMAIL_RECRUITER_HAPPY_PATH"]


# se obtiene el ID de la vacanbe regresado el mismo
def get_vacante_id():
    try:
        print('\ninicia el login del reclutador', email)
        _, headers, _ = login_recruiter(email)
        url = env[
                  "URL_SERVER"] + ('user/vacant/admin?pageSize=6&pageNumber=0&sortBy=publicationDate&sortDirection='
                                   'DESC&status=ACTIVA')
        response = send_get_headers(url, headers, 200)
        vacant_id = response["content"][0]["vacant"]["vacantId"]
        print('la vacanteId es: ' + vacant_id)
        return vacant_id
    except Exception as e:
        print('No se obtuvo la vacant Id', e)
        return 'No se obtuvo la vacant ID'


def get_questions_area_specialty(url, headers):
    print('Se obtiene las preguntas')
    respuesta = requests.get(url, headers=headers)
    data = respuesta.json()

    cantidad = len(data["content"])
    print('son', cantidad, 'preguntas\n')

    return cantidad, data


# se obtiene el id de las preguntas una vez que te postulas
def get_preguntas(url, headers):
    try:
        cantidad, data = get_questions_area_specialty(url, headers)
        questions = []

        for i in range(cantidad):

            exp = random.randint(0, 10)
            boleanos = [True, False]
            boleano = random.choice(boleanos)
            niveles = ['INTERMEDIO', 'AVANZADO', 'EXPERTO']
            nivel = random.choice(niveles)
            question_id = data['content'][i]['questionId']
            question_type_question = data['content'][i]['typeQuestion']
            question_type = data['content'][i]['type']
            question_year = data['content'][i]['yearsExperience']
            question_skill_level = data['content'][i]['skillLevel']

            if question_type_question == 'CERRADA':
                questions.append({
                    "question": {
                        "questionId": question_id
                    },
                    "value": boleano,
                    "binaryAnswer": boleano
                })

            elif question_type_question == 'ABIERTA':
                questions.append({
                    "question": {
                        "questionId": question_id
                    },
                    "value": "respuesta obtenida de una prueba automatizada",
                    "openAnswer": "respuesta obtenida de una prueba automatizada"
                })

            elif question_type == 'HARD_SKILL':
                if question_type_question == 'EXPERIENCIA':
                    if question_year is not None:
                        print('Son años de exp')
                        questions.append({
                            "question": {
                                "questionId": question_id
                            },
                            "value": question_year,
                            "yearsExperienceAnswer": question_year
                        })

                    elif question_skill_level is not None:
                        print('es de nivel')
                        questions.append({
                            "question": {
                                "questionId": question_id
                            },
                            "value": nivel,
                            "levelHardSkill": nivel
                        })

            elif question_type_question == 'EXPERIENCIA':
                questions.append({
                    "question": {
                        "questionId": question_id
                    },
                    "value": exp,
                    "yearsExperienceAnswer": exp
                })

            else:
                print(f'No hay respuesta para el tipo de pregunta {question_type_question}, {question_type}')
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
        postulation_id = send_post_headers_sin_body(url, headers, 200)
        if postulation_id != 0:
            print('la postulacion es: ', postulation_id)
            print('se hizo la postulacion correctamente\n')
            total = {"exito": 1, "fallo": 0}
            return 'se realizo la postulación a una vacante', postulation_id, total
        else:
            print('No se hizo la postulacion')
            total = {"exito": 0, "fallo": 1}
            return 'No se hizo la postulación a una vacante', None, total
    except Exception as e:
        print('No se hizo la postulacion', e)
        return 'No se hizo la postulación a una vacante', None, 0


# Se manda la experiencia laboral
def exp_laboral_cuestionario(headers, postulation_id):
    try:
        print('\nSe envia el cuestionario de experiencia laboral\n')

        url = (env[
                   "URL_SERVER"] + 'user/candidate/postulation/question?page=0&size=100&processId=' + postulation_id +
               '&questionnaire=AREA_SPECIALTY')
        print(url)
        my_body = get_preguntas(url, headers)
        url = (env[
                   "URL_SERVER"] + 'user/candidate/postulation/answer?processId=' + postulation_id +
               '&questionnaire=EXPERIENCE')
        resultado = send_post_headers(url, headers, my_body, 200)
        if resultado != 0:
            print('Se mandaron las respuestas del cuestionario :)\n', resultado)
            return 'Se manda respuesta de experiencia laboral', 1
        else:
            print('No se mando las respuestas del cuestionario :(\n')
            return 'no se mando las respuestas del cuestionario', 0
    except Exception as e:
        print('No se mando las respuestas del cuestionario :(\n', e)
        return 'no se mando las respuestas del cuestionario'


# se mandan las preguntas de habilidad profesional
def habilidad_profesional(headers, postulation_id):
    try:
        print('\ninicia las habilidades profesionales \n')
        url = (env[
                   "URL_SERVER"] + 'user/candidate/postulation/question?page=0&size=100&processId=' + postulation_id +
               '&questionnaire=HARD_SKILL')
        my_body = get_preguntas(url, headers)
        url = (env[
                   "URL_SERVER"] + 'user/candidate/postulation/answer?processId=' + postulation_id +
               '&questionnaire=HARD_SKILL')
        respuesta = send_post_headers(url, headers, my_body, 200)
        if respuesta != 0:
            print('se envio el cuestionario de habilidades profesionales :)\n', respuesta)
            return 'Se envian las respuestas de las habilidades profesionales', 1
        else:
            print('No se envian respuestas de las habilidades profesionales :(\n')
            return 'No se envian las habilidades profesionales', 0
    except Exception as e:
        print('No se envian respuestas de las habilidades profesionales :(\n', e)
        return 'No se envian las habilidades profesionales'


def habilidad_blandas(headers, postulation_id):
    try:
        print('\ninicia las habilidades blandas \n')
        url = (env[
                   "URL_SERVER"] + 'user/candidate/postulation/question?page=0&size=100&processId=' + postulation_id +
               '&questionnaire=SOFT_SKILL')

        my_body = get_preguntas(url, headers)
        url = (env[
                   "URL_SERVER"] + 'user/candidate/postulation/answer?processId=' + postulation_id +
               '&questionnaire=SOFT_SKILL')
        respuesta = send_post_headers(url, headers, my_body, 200)
        if respuesta != 0:
            print('se envia las respuestas del habilidades blandas :)\n ', respuesta)
            return 'Se envian las respuestas de las habilidades blandas', 1
        else:
            print('No se envia las respuestas de las habilidades balndas :(\n')
            return 'No se envia las respuestas de las habilidades balndas', 0
    except Exception as e:
        print('No se envia las respuestas de las habilidades balndas :(\n', e)
        return 'No se envia las respuestas de las habilidades balndas', 0


# se manda la expectativa salarial
def expectativa_salarial(headers, postulation_id):
    try:
        print('\nInicia la espectava salarial :)\n')
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
        if respuesta != 0:
            print('Se manda la espectativa salarial :)\n', respuesta)
            return 'Se envia la espectativa salarial correctamente', 1
        else:
            print('No se mando la espectativa salarial :(\n')
            return 'No se manda la espectativa salarial', 0
    except Exception as e:
        print('No se mando la espectativa salarial :(\n', e)
        return 'No se manda la espectativa salarial', 0


# se manda las condiciones de contratacion
def condiciones_de_contratacion(headers, postulation_id):
    try:
        print('\nInicia el egistro de condiciones de contratación')
        url = env["URL_SERVER"] + 'user/candidate/postulation/contract-conditions'
        my_body = {
            "selectionProcessId": postulation_id,
            "completeContractConditions": True,
            "detailsContractConditions": "tengo todo"
        }
        respuesta = send_post_headers(url, headers, my_body, 200)
        if respuesta != 0:
            print('Se mandan las condiciones de contratación :)\n', respuesta)
            return 'Se envian las condiciones de contratación, correctamente', 1
        else:
            print('No se mandan las condiciones de contratacion :(\n')
            return 'No se mandan las condiciones de contratacion', 0
    except Exception as e:
        print('No se mandan las condiciones de contratacion :(\n', e)
        return 'No se mandan las condiciones de contratacion', 0


# se manda los permisos de video presentacion y video entrevista
def seleccion_de_permisos(headers, postulation_id):
    try:
        print('\nSe inicia la seccion de permisos de videos y psicometricas')
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
        if respuesta != 0:
            print('Se mandan los permisos de postulacion :)\n', respuesta)
            return 'Se envian los permisos de postulación', 1
        else:
            print('No se mandan los permisos de postulacion :( \n')
            return 'No se mandan los permisos de postulación', 0
    except Exception as e:
        print(f'No se mandan los permisos de postulacion :( {e} \n')
        return 'No se mandan los permisos de postulación', 0


def change_permission_postulation(headers, postulation_id):
    try:
        print('\nSe inicia el cambio de permisos de videos y psicometricas \n')
        url = env["URL_SERVER"] + 'user/permissions/selection-process?selectionProcessId=' + postulation_id
        my_body = [
            {
                "permissionType": "VIDEOPRESENTATION_SHARE",
                "status": True
            },
            {
                "permissionType": "VIDEOINTERVIEW",
                "status": True
            }
        ]
        respuesta = send_post_headers(url, headers, my_body, 200)
        if respuesta != 0:
            print('Se cambian los permisos de postulacion :)\n', respuesta)
            return 'Se cambian los permisos de postulación', 1
        else:
            print('No se cambian los permisos de postulacion :(\n')
            return 'No se cambian los permisos de postulación', 0
    except Exception as e:
        print(f'No se cambian los permisos de postulacion :( {e} \n')
        return 'No se cambian los permisos de postulación', 0


def get_questions_vp():
    print('\nInicia el cuestionario de la video presentación')
    response = requests.get(env["URL_SERVER"] + "management/catalog/question-presentation")
    if response != 0:
        # Cargar la respuesta JSON
        json_dict = response.json()

        # Agregar la clave isSelected: True a cada pregunta
        for question in json_dict:
            question["isSelected"] = True

        # Seleccionar 2 preguntas aleatoriamente
        selected_questions = random.sample(json_dict, 2)

        # Retornar las 2 preguntas seleccionadas aleatoriamente
        return selected_questions
    else:
        print('No se obtuvieron las preguntas')
        return 'No se obtuvieron las preguntas'


def upload_video_presentacion(headers):
    try:
        print('\nSe sube el video de  la presentacion del candidato \n')
        url = env["URL_SERVER"] + 'files/upload/presentation-video'
        ruta = videos()
        response = subir_archivo(ruta, url, headers, 200)
        if response != 0:
            print('Se subio el video de presentacion:)', response)
            return 'Se subio el video de presentacion correctamente'
        else:
            print('No se subio la video presentacion :(\n')
            return 'No se subio la video presentacion'
    except Exception as e:
        print('No se subio la video presentacion :(\n', e)
        return 'No se subio la video presentacion'


def upload_questions_video_presentation(headers):
    try:
        print('\ninicia la carga de la video presentacion\n')
        url = env["URL_SERVER"] + 'user/candidate/questions-presentation'
        my_body = get_questions_vp()
        respuesta = send_post_headers(url, headers, my_body, 200)
        if respuesta != 0:
            upload_video_presentacion(headers)
            print(f'Se sube la video presentacion {respuesta} \n')
            return 'Se sube la video presentación', 1
        else:
            print('No se subio la video presentación \n')
            return 'No se subio la video presentación', 0
    except Exception as e:
        print(f'No se subio la video presentación {e} \n')
        return 'No se subio la video presentación', 0


def upload_video_interview(headers, postulation_id):
    try:
        print('\ninicia la subida de la video entrevista \n')
        url = env["URL_SERVER"] + 'files/upload/interview-video?selectionProcessId=' + str(postulation_id)
        print(url)
        ruta = videos()
        response = subir_archivo(ruta, url, headers, 200)
        if response != 0:
            print(f'Se subio la video entrevista {response} \n')
            return 'Se sube la video entrevista', 1
        else:
            print('No se subio la video entrevista \n')
            return 'No se subio la video entrevista', 0
    except Exception as e:
        print(f'No se subio la video entrevista {e}\n')
        return 'No se subio la video entrevista', 0


def delete_postulation(headers, postulation_id):
    try:
        print('\ninicia la eliminación de postulacion')
        url = env["URL_SERVER"] + 'user/candidate/postulation?selectionProcessId=' + postulation_id
        respuesta = send_delete_sin_body(url, headers, 200)
        if respuesta != 0:
            print('Se elimino la postulación')
            return 'Se elimino la postulacion', 1
        else:
            print('No se hizo la eliminacion de la postulación')
            return 0
    except Exception as e:
        print('No se hizo la postulación', e)
        return 'No se hizo la postulacion', 0
