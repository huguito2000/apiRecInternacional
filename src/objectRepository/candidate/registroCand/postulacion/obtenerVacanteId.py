import random
from src.modules.Reclutador.loginRecruiter import login_recruiter
from src.services.funciones import send_get, base, send_post_headers_sin_body, send_post_headers, salary_min

correo = '2205qa@yopmail.com'


# se obtiene el ID de la vacanbe regresado el mismo
def vacante_id():
    try:
        _, headers, _ = login_recruiter(correo)
        url = base + 'user/vacant/admin?pageSize=6&pageNumber=0&sortBy=publicationDate&sortDirection=DESC&status=ACTIVA'
        response = send_get(url, headers, 200)
        vacant_id = response["content"][0]["vacant"]["vacantId"]
        print('la vacanteId es:' + vacant_id)
        return vacant_id
    except Exception as e:
        print('No se obtuvo la vacanteId', e)
        return 'No se obtuvo la vacante ID'


# se obtiene el id de las preguntas una vez que te postulas
def get_preguntas(headers, url, cantidad):
    try:

        questions: list = []
        resultado = send_get(url, headers, 200)

        for i in range(cantidad):
            questions.append(resultado['content'][i]['questionId'])
        print('Se obtienen los Ids de las preguntas')
        return questions
    except Exception as e:
        print('No se pudo obtener los ids de las vacantes', e)
        return 'No se pudo obtener los ids de las vacantes'



# Se hace la postulacion de la primera vacante que se encuentra
def postulacion(headers):
    try:
        vacant_id = vacante_id()

        url = base + 'user/candidate/postulation?vacantId=' + vacant_id
        print(url)
        postulation_id = send_post_headers_sin_body(url, headers, 200)
        print(postulation_id)
        print('se hizo la postulacion correctamente')
        return postulation_id
    except Exception as e:
        print('No se hizo la postulacion', e)
        return 'No se hizo la postulación'



# se saca de manera aleatoria un nuemro entre el rango de 1 a 5
def experiencia():
    exp = random.randint(1, 5)
    return exp


# Se manda la experiencia laboral
def exp_laboral_cuestionario(headers, postulation_id):
    try:
        exp1 = int(experiencia())
        exp2 = int(experiencia())
        url = base + 'user/candidate/postulation/question?page=0&size=100&processId=' + postulation_id + '&questionnaire=AREA_SPECIALTY'

        preguntas = get_preguntas(headers, url, 3)

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
                    "questionId": "e6ca27d3-22b0-4666-8708-fbc2d08a7731"
                },
                "value": exp2,
                "yearsExperienceAnswer": exp2
            },
            {
                "question": {
                    "questionId": "f6fa3592-8cd7-48ad-b50a-58aec720afc1"
                },
                "value": True,
                "binaryAnswer": True
            }
        ]

        url = base + 'user/candidate/postulation/answer?processId=' + postulation_id + '&questionnaire=EXPERIENCE'
        print(url)
        print(my_body)
        resultado = send_post_headers(url, headers, my_body, 200)
        print('Se mandaron las respuestas del cuentionario', resultado)
        return 'Se mandaron las respuestas del cuestionario'
    except Exception as e:
        print('No se mando las respuestas del cuestionario', e)
        return e



# se obtienen los niveles aleatoriamente
niveles = ['INTERMEDIO', 'AVANZADO', 'EXPERTO']
nivel = random.choice(niveles)


# se mandan las preguntas de habilidad profesional
def habilidad_profesional(headers, postulation_id):
    try:
        print('inicia las habilidades profecionales')
        url = base + 'user/candidate/postulation/question?page=0&size=100&processId=' + postulation_id + '&questionnaire=HARD_SKILL'

        preguntas = get_preguntas(headers, url, 1)
        print(preguntas)
        my_body = [
            {
                "question": {
                    "questionId": preguntas[0]
                },
                "value": nivel,
                "levelHardSkill": nivel
            }
        ]
        print(my_body)
        url = base + 'user/candidate/postulation/answer?processId=' + postulation_id + '&questionnaire=HARD_SKILL'
        respuesta = send_post_headers(url, headers, my_body, 200)
        print(respuesta)
        return 'Se mandan las habilidades profecionales'
    except Exception as e:
        print('No se manadas las habilidades profecionales', e)
        return 'No se manadas las habilidades profecionales'


# se manda la expectativa salarial
def expectativa_salarial(headers, postulation_id):
    try:
        salario_min = salary_min()
        url = base + 'user/candidate/postulation/salary-expectation'
        my_body = {
            "selectionProcessId": postulation_id,
            "salaryMin": salario_min,
            "salaryMax": None,
            "periodicityId": "4028818e8e337efb018e33801b680005",
            "currencyId": "2c9f9364867665940186849ddb990011"
        }

        respuesta = send_post_headers(url, headers, my_body, 200)
        print('Se manda la espectativa salarial', respuesta)
        return 'Se manda la espectativa salarial'
    except Exception as e:
        print('No se mando la espectativa salarial', e)
        return 'No se manda la espectativa salarial'


# se manda las condiciones de contratacion
def condiciones_de_contratacion(headers, postulation_id):
    try:
        url = base + 'user/candidate/postulation/contract-conditions'
        my_body = {
            "selectionProcessId": postulation_id,
            "completeContractConditions": True,
            "detailsContractConditions": "tengo todo"
        }

        respuesta = send_post_headers(url, headers, my_body, 200)
        print('Se mandan las condicoones de contratación', respuesta)
        return 'Se mandanlas condiciones de contratacion'
    except Exception as e:
        print('No se mandan las condiciones de contratacion', e)


# se manda los permisos de video presentacion y video entrevista
def seleccion_de_permisos(headers, postulation_id):
    try:
        url = base + 'user/permissions/selection-process?selectionProcessId=' + postulation_id
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
        print('Se mandan los permisos de postulacion', respuesta)
        return 'Se mandan los permisos de postulacion'
    except Exception as e:
        print('No se mandan los permisos de postulacion', e)
        return 'No se mandan los permisos de postulación'

