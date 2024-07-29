from src.object_repository.candidate.registroCand.registerValid.my_cv.stepCVFull import work_experience, education, \
    area_experience, hard_skills, course, soft_skills, certificate, language
from src.services.catalogs import data_user, env
from src.services.peticiones_HTTP import base, send_post_headers, send_put_body


name, last_name, _, birth_date, email_candidate = data_user(env)

data_exp_word = [
    {
        "company": "",
        "dateDeparture": None,
        "dateEntry": str(birth_date),
        "dependents": False,
        "functions": "hola mundo",
        "numberDependents": 0,
        "position": {
            "position": "tester"
        },
        "positionType": {
            "positionTypeId": "40288086796be11e01796c18e66f0064"
        },
        "working": True,
        "candidateId": "ff8080818e9a6892018e9a743f60001b"
    },
    {"company": " ",
     "dateDeparture": None,
     "dateEntry": str(birth_date),
     "dependents": False,
     "functions": "hola mundo1 ",
     "numberDependents": 0,
     "position": {
         "position": "tester"
     },
     "positionType": {
         "positionTypeId": "40288086796be11e01796c18e66f0064"
     },
     "working": True,
     "candidateId": "ff8080818e9a6892018e9a743f60001b"
     },
    {"company": "involve",
     "dateDeparture": None,
     "dateEntry": str(birth_date),
     "dependents": False,
     "functions": " ",
     "numberDependents": 0,
     "position": {
         "position": "tester"
     },
     "positionType": {
         "positionTypeId": "40288086796be11e01796c18e66f0064"
     },
     "working": True,
     "candidateId": "ff8080818e9a6892018e9a743f60001b"

     },
    {"company": "involve",
     "dateDeparture": None,
     "dateEntry": str(birth_date),
     "dependents": False,
     "functions": "hola mundo 2 ",
     "numberDependents": 0,
     "position": {
         "position": "tester"
     },
     "positionType": {
         "positionTypeId": "40288086796be11e01796c18e66f0064"
     },
     "working": True,
     "candidateId": "ff8080818e9a6892018e9a743f60001b"

     },
    {"company": "involve",
     "dateDeparture": None,
     "dateEntry": "2050-12-12",
     "dependents": False,
     "functions": "hola mundo ",
     "numberDependents": 0,
     "position": {
         "position": "tester"
     },
     "positionType": {
         "positionTypeId": "40288086796be11e01796c18e66f0064"
     },
     "working": True,
     "candidateId": "ff8080818e9a6892018e9a743f60001b"

     },
    {"company": "involve",
     "dateDeparture": None,
     "dateEntry": "2050-12-12",
     "dependents": False,
     "functions": "hola mundo ",
     "numberDependents": 0,
     "position": {
         "position": ""
     },
     "positionType": {
         "positionTypeId": "40288086796be11e01796c18e66f0064"
     },
     "working": True,
     "candidateId": "ff8080818e9a6892018e9a743f60001b"

     }
]


def word_exp_400(headers, data, code):
    try:
        url = base + 'user/candidate/work-experience'
        respuesta = send_post_headers(url, headers, data_exp_word, code)
        print(f"Resultado con datos: {data}, código: {code}")
        print(f'Se manda la seccion de experiencia laboral con respuesta {respuesta}')
    except Exception as e:
        print(f'No se envio la experiencia laboral del candidato {e}')
        return f'No se envio experiencia laboraldel candidato {e}'


def work_experience_data_no_valid(headers):
    try:
        print('\nSe Envia la seccion de experiencia laboral de manera incorrecta')
        for data in data_exp_word:
            word_exp_400(headers, data, 400)
        work_experience(headers)
        print('Se enviaron las prueba de experiencia laboral')
        return 'Se manda la experiencia laboral del candidato'
    except Exception as e:
        print('No paso la experiencia laboral', e)
        return 'No paso la experiancia laboral del candidato'


data_education = [
    {
        "educationStatus": {
            "catalogSystemId": "4028818e8e3e2d7c018e3e2ded120010",
            "name": "",
            "type": "educationStatus",
            "level": 5,
            "status": True,
            "keySystem": None,
            "shown": True
        },
        "educationLevel": {
            "catalogSystemId": "4028818e8e3e2d7c018e3e2de60f000a",
            "name": "Doctorado",
            "type": "educationLevel",
            "level": 8,
            "status": True,
            "keySystem": None
        },
        "countryInstitute": "México",
        "degree": "ingeniero",
        "instituteName": "unam",
        "startYear": "2010",
        "endYear": "2015",
        "candidateId": "ff8080818e9f641f018e9fa35d270022",
        "institute": {
            "name": "(enap) hoy (fad) de la unam",
            "idInstitution": "2c9fc61583f3fea50184e357a04e7db7",
            "codeCountry": "mx"
        }
    }, {
        "educationStatus": {
            "catalogSystemId": "4028818e8e3e2d7c018e3e2ded120010",
            "name": "Titulado",
            "type": "educationStatus",
            "level": 5,
            "status": True,
            "keySystem": None,
            "shown": True
        },
        "educationLevel": {
            "catalogSystemId": "4028818e8e3e2d7c018e3e2de60f000a",
            "name": "Doctorado",
            "type": "educationLevel",
            "level": 8,
            "status": False,
            "keySystem": None
        },
        "countryInstitute": "México",
        "degree": "ingeniero",
        "instituteName": "unam",
        "startYear": "2010",
        "endYear": "2015",
        "candidateId": "ff8080818e9f641f018e9fa35d270022",
        "institute": {
            "name": "(enap) hoy (fad) de la unam",
            "idInstitution": "2c9fc61583f3fea50184e357a04e7db7",
            "codeCountry": "mx"
        }
    }, {
        "educationStatus": {
            "catalogSystemId": "4028818e8e3e2d7c018e3e2ded120010",
            "name": "Titulado",
            "type": "educationStatus",
            "level": 5,
            "status": True,
            "keySystem": None,
            "shown": True
        },
        "educationLevel": {
            "catalogSystemId": "4028818e8e3e2d7c018e3e2de60f000a",
            "name": "Doctorado",
            "type": "educationLevel",
            "level": 8,
            "status": True,
            "keySystem": None
        },
        "countryInstitute": "México",
        "degree": "ingeniero",
        "instituteName": "unam",
        "startYear": "2080",
        "endYear": "3095",
        "candidateId": "ff8080818e9f641f018e9fa35d270022",
        "institute": {
            "name": "(enap) hoy (fad) de la unam",
            "idInstitution": "2c9fc61583f3fea50184e357a04e7db7",
            "codeCountry": "mx"
        }
    }
]


def education_400(headers, data, code):
    try:
        url = base + 'user/candidate/education'
        respuesta = send_post_headers(url, headers, data_education, code)
        print(f"Resultado con datos: {data}, código: {code}")
        print(f'Se mandas la seccion de experiencia laboral con respuesta {respuesta}')
    except Exception as e:
        print(f'No se envio la educacion del candidato {e}')
        return f'No se envio la educacion del candidato {e}'


def education_data_no_valid(headers):
    try:
        print('\nSe Envia la seccion de educación de manera incorrecta')
        for data in data_education:
            education_400(headers, data, 400)
        education(headers)
        print('Se enviaron las prueba de educacion')
        return 'Se manda la educacionl del candidato'
    except Exception as e:
        print('No paso la educacion', e)
        return 'No paso la educacion del candidato'


data_areas_experience = [
    {
        "areaId": "40288087797b055a01797b14e5f40036",
        "name": "Tecnología de la información",
        "specialties": [
            {
                "specialtyId": "4028808d7c3882b0017cb4464e099434",
                "name": "QA",
                "areaId": ""
            }
        ]
    }, {
        "areaId": " ",
        "name": "Tecnología de la información",
        "specialties": [
            {
                "specialtyId": "4028808d7c3882b0017cb4464e099434",
                "name": "QA",
                "areaId": "40288087797b055a01797b14e5f40036"
            }
        ]
    }, {
        "areaId": "40288087797b055a01797b14e5f40036",
        "name": "Tecnología de la información",
        "specialties": [
            {
                "specialtyId": "",
                "name": "QA",
                "areaId": "40288087797b055a01797b14e5f40036"
            }
        ]
    }, {
        "areaId": "93842398423894723894729384",
        "name": "Tecnología de la información",
        "specialties": [
            {
                "specialtyId": "4028808d7c3882b0017cb4464e099434",
                "name": "QA",
                "areaId": "40288087797b055a01797b14e5f40036"
            }
        ]
    },

]


def areas_experience_400(headers, data, code):
    try:
        url = base + 'user/candidate/area'
        respuesta = send_post_headers(url, headers, data_areas_experience, code)
        print(f"Resultado con datos: {data}, código: {code}")
        print(f'Se mandas la sección de areas de experiencia con respuesta {respuesta}')
    except Exception as e:
        print(f'No se envio las areas de experiencia del candidato {e}')
        return f'No se envio las areas de experiencia del candidato {e}'


def areas_experience_data_no_valid(headers):
    try:
        print('\nSe Envia la seccion de areas de experiencia de manera incorrecta')
        for data in data_areas_experience:
            areas_experience_400(headers, data, 409)
        area_experience(headers)
        print('Se enviaron las prueba de las areas de experiencia')
        return 'Se manda  las areas de experiencia del candidato'
    except Exception as e:
        print('No paso las areas de experiencia', e)
        return 'No paso las areas de experiencia del candidato'


data_hard_skill = [
    {
        "level": "",
        "skill": "Conocimiento avanzado de Microsoft Excel. "
    }, {
        "level": "EXPERTO",
        "skill": ""
    },
    {
        "level": "EXPERTO hola mundo",
        "skill": "Conocimiento avanzado de Microsoft Excel. dsadsadasdadasdas "
    }
]


def hard_skill_400(headers, data, code):
    try:
        url = base + 'user/candidate/hard-skill'
        respuesta = send_post_headers(url, headers, data_hard_skill, code)
        print(f"Resultado con datos: {data}, código: {code}")
        print(f'Se mandas la sección de habilidades duras con respuesta {respuesta}')
    except Exception as e:
        print(f'No se envio las habiidades duras del candidato {e}')
        return f'No se envio las habilidades duras del candidato {e}'


def hard_skill_data_no_valid(headers):
    try:
        print('\nSe Envia la seccion de habiliadses duras de manera incorrecta')
        for data in data_hard_skill:
            hard_skill_400(headers, data, 400)
        hard_skills(headers)
        print('Se enviaron las prueba de las habilidades duras')
        return 'Se manda  las areas de las habilidades duras'
    except Exception as e:
        print('No paso las areas de las habilidades duras', e)
        return 'No paso las areas de las habilidades duras'


data_course = {
    "dateExpedition": "2040-12-12",
    "hours": "82",
    "insitute": "udemy",
    "name": "istbq"
}


def course_400(headers, data, code):
    try:
        url = base + 'user/candidate/course'
        respuesta = send_put_body(url, headers, data_course, code)
        print(f"Resultado con datos: {data}, código: {code}")
        print(f'Se manda el curso con respuesta {respuesta}')
    except Exception as e:
        print(f'No se envio los cursos del candidato {e}')
        return f'No se envio los cursos del candidato {e}'


def course_data_no_valid(headers):
    try:
        print('\nSe Envia la seccion de cursos de manera incorrecta')
        for data in data_course:
            course_400(headers, data, 400)
        course(headers)
        print('Se enviaron las prueba de los cursos')
        return 'Se manda  las areas de los cursos'
    except Exception as e:
        print('No paso las areas de los cursos', e)
        return 'No paso las areas de los cursos'


data_soft_skills = [
    {
        "skill": "Trabajo en equipo",
    }, {
        " "
    }
]


def soft_skills_400(headers, data, code):
    try:
        url = base + 'user/candidate/soft-skill'
        respuesta = send_post_headers(url, headers, data_soft_skills, code)
        print(f"Resultado con datos: {data}, código: {code}")
        print(f'Se manda la sección de habilidades blandas con respuesta {respuesta}')
    except Exception as e:
        print(f'No se envio las habiidades blandas del candidato {e}')
        return f'No se envio las habilidades blandas del candidato {e}'


def soft_skills_data_no_valid(headers):
    try:
        print('\nSe Envia la seccion de habilidades blandas de manera incorrecta')
        for data in data_soft_skills:
            hard_skill_400(headers, data, 400)
        soft_skills(headers)
        print('Se enviaron las prueba de las habilidades blandas')
        return 'Se manda  las areas de las habilidades blandas'
    except Exception as e:
        print('No paso la sección de las habilidades blandas', e)
        return 'No paso la sección de las habilidades blandas'


data_certificate = [
    {
        "credentialId": "udemy121212",
        "institute": "IPN",
        "dateExpedition": "2022-12-12",
        "dateExpire": "",
        "name": "istbq",
        "url": "www.google.com",
        "isExpire": False,
        "candidateCertificationId": "ff8080818b82167a018bb0cf881300fc"
    }, {
        "credentialId": "   ",
        "institute": "IPN",
        "dateExpedition": "2022-12-12",
        "dateExpire": "",
        "name": "istbq",
        "url": "www.google.com",
        "isExpire": False,
        "candidateCertificationId": "ff8080818b82167a018bb0cf881300fc"
    }, {
        "credentialId": "udemy121212",
        "institute": "IPN",
        "dateExpedition": "2050-12-12",
        "dateExpire": "",
        "name": "istbq",
        "url": "www.google.com",
        "isExpire": False,
        "candidateCertificationId": "ff8080818b82167a018bb0cf881300fc"
    }, {
        "credentialId": "udemy121212",
        "institute": "IPN",
        "dateExpedition": "2022-12-12",
        "dateExpire": "1922-12-12",
        "name": "istbq",
        "url": "www.google.com",
        "isExpire": False,
        "candidateCertificationId": "ff8080818b82167a018bb0cf881300fc"
    }
]


def certificate_400(headers, data, code):
    try:
        url = base + 'user/candidate/certification'
        respuesta = send_post_headers(url, headers, data_certificate, code)
        print(f"Resultado con datos: {data}, código: {code}")
        print(f'Se manda la sección de certificado con respuesta {respuesta}')
    except Exception as e:
        print(f'No se envio el certificado del candidato {e}')
        return f'No se envio el certificado del candidato {e}'


def certificate_data_no_valid(headers):
    try:
        print('\nSe Envia la seccion de certificado de manera incorrecta')
        for data in data_certificate:
            certificate_400(headers, data, 400)
        certificate(headers)
        print('Se enviaron las prueba del certificado')
        return 'Se manda  las areas del certificado'
    except Exception as e:
        print('No paso la sección  del certificado', e)
        return 'No paso la sección de certificado'


data_language = [
    {
        "language": {
            "languageId": "402880de7abf2e1e017abf8cdc1e0000",
            "spanishName": "Africano"
        },
        "level": "NATIVO"
    },
    {
        "language": {
            "languageId": "  ",
            "spanishName": "Africano"
        },
        "level": "NATIVO"
    },
    {
        "language": {
            "languageId": "402880de7abf2e1e017abf8cdc1e0000",
            "spanishName": "  "
        },
        "level": "NATIVO"
    },
    {
        "language": {
            "languageId": "402880de7abf2e1e017abf8cdc1e0000",
            "spanishName": "Africano"
        },
        "level": " "
    }
]



def language_400(headers, data, code):
    try:
        url = base + 'user/candidate/language'
        respuesta = send_post_headers(url, headers, data_language, code)
        print(f"Resultado con datos: {data}, código: {code}")
        print(f'Se manda la sección de lenguaje con respuesta {respuesta}')
    except Exception as e:
        print(f'No se envio del lenguaje del candidato {e}')
        return f'No se envio del lenguaje del candidato {e}'


def language_data_no_valid(headers):
    try:
        print('\nSe Envia la seccion de lenguaje de manera incorrecta')
        for data in data_language:
            language_400(headers, data, 400)
        language(headers)
        print('Se enviaron las prueba del lenguaje')
        return 'Se manda  las areas del lenguaje'
    except Exception as e:
        print('No paso la sección  del lenguaje', e)
        return 'No paso la sección de lenguaje'









